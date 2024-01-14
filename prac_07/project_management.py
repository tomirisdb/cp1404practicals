import datetime

class Project:
    def __init__(self, name, completion, priority, start_date):
        self.name = name
        self.completion = completion
        self.priority = priority
        self.start_date = start_date

    def __str__(self):
        return f"{self.name} - {self.completion}% completed, Priority: {self.priority}, Start Date: {self.start_date}"

    def __lt__(self, other):
        return self.priority < other.priority


def main():
    file_name = 'projects.txt'
    projects = load_projects(file_name)

    while True:
        print("\nMenu:")
        print("1. Load Projects")
        print("2. Save Projects")
        print("3. Display Projects")
        print("4. Filter Projects by Date")
        print("5. Add New Project")
        print("6. Update Project")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            file_name = input("Enter the filename to load projects from: ")
            projects = load_projects(file_name)
        elif choice == '2':
            file_name = input("Enter the filename to save projects to: ")
            save_projects(file_name, projects)
        elif choice == '3':
            display_projects(projects)
        elif choice == '4':
            date_filter = datetime.datetime.strptime(input("Enter the filter date (d/m/yyyy): "), "%d/%m/%Y").date()
            filter_projects_by_date(projects, date_filter)
        elif choice == '5':
            add_new_project(projects)
        elif choice == '6':
            update_project(projects)
        elif choice == '7':
            save_projects(file_name, projects)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


def load_projects(file_name):
    projects = []
    try:
        with open(file_name, 'r') as file:
            file.readline()  # Skip header
            for line in file:
                parts = line.strip().split('\t')

                # Check if there are exactly four elements in parts
                if len(parts) == 4:
                    name, completion, priority, start_date = parts
                    project = Project(name, int(completion), int(priority), datetime.datetime.strptime(start_date, "%d/%m/%Y").date())
                    projects.append(project)
                else:
                    print(f"Skipping invalid line.")

    except FileNotFoundError:
        pass  # Handle the case where the file does not exist
    return projects


def save_projects(file_name, projects):
    with open(file_name, 'w') as file:
        file.write("Name\tCompletion\tPriority\tStart Date\n")
        for project in projects:
            file.write(f"{project.name}\t{project.completion}\t{project.priority}\t{project.start_date.strftime('%d/%m/%Y')}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("\nIncomplete Projects:")
    for project in sorted(incomplete_projects):
        print(project)

    print("\nCompleted Projects:")
    for project in completed_projects:
        print(project)

def filter_projects_by_date(projects, date_filter):
    filtered_projects = [project for project in projects if project.start_date > date_filter]
    print("\nFiltered Projects:")
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(project)

def add_new_project(projects):
    name = input("Enter the project name: ")
    completion = int(input("Enter the completion percentage: "))
    priority = int(input("Enter the priority: "))
    start_date = datetime.datetime.strptime(input("Enter the start date (d/m/yyyy): "), "%d/%m/%Y").date()
    new_project = Project(name, completion, priority, start_date)
    projects.append(new_project)
    print("New project added successfully.")

def update_project(projects):
    project_name = input("Enter the project name to update: ")
    for project in projects:
        if project.name.lower() == project_name.lower():
            new_completion = input("Enter the new completion percentage (leave blank to retain existing value): ")
            new_priority = input("Enter the new priority (leave blank to retain existing value): ")

            if new_completion:
                project.completion = int(new_completion)
            if new_priority:
                project.priority = int(new_priority)

            print("Project updated successfully.")
            return

    print("Project not found.")

if __name__ == "__main__":
    main()

