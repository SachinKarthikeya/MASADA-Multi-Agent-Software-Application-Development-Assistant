# 🧑‍💻 MASADA - Multi-Agent Software Application Development Assistant

An efficient multi-agent system where if a user has a project idea but don't know where to start from, our agents help them plan, code, test, review and deploy an initial version of their application from scratch. This helps developers and testers get the inital architecture, source code, improvement feedbacks and deploying and testing strategies of the project they want to develop and test.

## 🚀 Features

- **CrewAI**: Multi-Agent Framework to orchestrate AI Agent workflows
- **Llama3.2:1b**: The base LLM that is connected to the agents
- **Streamlit**: An interactive dashboard for the users
- Five agents: **Planner**, **Developer**, **Tester**, **Reviewer** and **Deployer** work together
- Users can download the generated project files in Markdown format

## 📄 Workflow

- Users enter their project idea along with their requirements if any.
- Five following agents work together in sequential order, managed by CrewAI:

- **Planner Agent**: Breaks down the given project idea into strategic development steps such as features, tools, technologies and data sources required for efficient development process.

- **Developer Agent**: Analyzes the development plan from the planner agent and develops an initial project which includes project structure, source codes, configuration files, etc. If the user did not mention his requirements, the agent automatically uses simpler yet efficient requirements to develop the project.

- **Tester Agent**: Tests the initial project developed by the developer agent using Unit Testing, Integration Testing, etc and generates a report which includes potential bugs or issues found and performance bottlenecks involved.

- **Reviewer Agent**: Reviews the application along with the testing report and provides feedback to improve the application using constraints such as Performance, Security, Maintainability, etc.

- **Deployer Agent**: Generates a detailed deployment plan such as containerization and CI/CD pipeline configurations to deploy the application after the user upgrades his application, or even the initial application to the production environment, along with best practices of secure and scalable deployment.

- The outputs of the work done by each agent is displayed on Streamlit dashboard.
- Users can download the generated project files in Markdown (.md) format for further manual upgrades.

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend Framework**: CrewAI
- **LLM**: Llama3.2:1b

## 📢 Future Enhancements

- Add more agents for in-detail breakdown and robust development of project
- Download code files in respective language formats
