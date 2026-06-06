from crewai import Agent, Task, Crew, Process

from llm_config import llm_model

llm = llm_model()

planner_agent = Agent(
    role = "Senior Software Architect",
    goal = "Break down the app idea into clear and strategic development steps, ensuring a well-structured and efficient development process",
    backstory = "You are a experienced software architect with a strong background in planning and designing software projects. You have a deep understanding of various tools, technologies, and data sources, and you excel at breaking down complex ideas into simple and actionable steps.",
    verbose = True,
    allow_delegation = False,
    llm = llm
)
developer_agent = Agent(
    role = "Senior Software Developer",
    goal = "Develop the software application based on the defined requirements and development steps, ensuring high-quality code and adherence to best practices throughout the development process",
    backstory = "You are an expert software developer with a strong background in building scalable and maintainable software solutions. You have a deep understanding of programming languages, frameworks, and development methodologies, and you excel at translating requirements into robust code.",
    verbose = True,
    allow_delegation = False,
    llm = llm
)
tester_agent = Agent(
    role = "Senior QA Engineer",
    goal = "Test the developed software application to ensure it meets the defined requirements and quality standards, identifying and reporting any issues or bugs that need to be addressed",
    backstory = "You are an experienced QA engineer with a strong background in testing software applications. You have a keen eye for detail and a deep understanding of testing methodologies, and you excel at ensuring that software applications meet high-quality standards.",
    verbose = True,
    allow_delegation = False,
    llm = llm
)
reviewer_agent = Agent(
    role = "Senior Code Reviewer",
    goal = "Review the developed software application to ensure it meets the defined requirements and quality standards, identifying and reporting any issues or bugs that need to be addressed",
    backstory = "You are an experienced code reviewer with a strong background in evaluating software code for quality, maintainability, and security. You have a deep understanding of software development principles, and you excel at ensuring that code meets high-quality standards.",
    verbose = True,
    allow_delegation = False,
    llm = llm
)

planning_task = Task(
    description = """
    Break down the following project idea into clear and strategic development steps:
    {project_idea}
    
    Include the following in your breakdown:
    1. Key deliverables
    2. Features 
    3. Required tools, technologies, and data sources
    """,
    expected_output = "A well-structured breakdown of the project idea into actionable development steps, including expected deliverables, features, tools, and technologies.",
    agent = planner_agent
)
developing_task = Task(
    description = """
    Based on the planner's breakdown, develop the software application by generating:
    1. Folder Structure
    2. Core Sample Code
    3. Key Modules

    If the project can be built efficiently using simpler data sources, tools or technologies, prioritize those over more complex options. 
    If the user has provided specific requirements or constraints, ensure that the developed software application adheres to those. If not, use simple yet efficient tools, technologies, and data sources to build the application.
    """,
    expected_output = "A fully developed software application that meets the defined requirements with clean, modular and production-ready code.",
    agent = developer_agent
)
testing_task = Task(
    description = """
    Test the software application built by the developer to ensure it meets the defined requirements and quality standards. Identify:

    1. Potential bugs or issues 
    2. Edge Cases
    """,
    expected_output = "A comprehensive testing report that identifies any bugs, issues and edge cases.",
    agent = tester_agent
)
reviewing_task = Task(
    description = """
    Based on the testing report and the developed software application, provide text-based feedback on the software application. Focus on:
    
    1. Readability
    2. Performance
    3. Security

    DO NOT confuse your task with tester agent's task i.e., identifying bugs or perform testing. You are a code reviewer, not a tester.
    """,
    expected_output = "Effective text-based feedback on the software application, providing suggestions for improving performance, readability and security.",
    agent = reviewer_agent
)

def assemble_crew():
    tech_crew = Crew(
        agents=[planner_agent, developer_agent, tester_agent, reviewer_agent],
        tasks=[planning_task, developing_task, testing_task, reviewing_task],
        process=Process.sequential
    )
    return tech_crew    llm = llm
)
deployer_agent = Agent(
    role = "Senior DevOps Engineer",
    goal = "Deploy the final software application to a production environment, ensuring a smooth and efficient deployment process while adhering to best practices for security and scalability",
    backstory = "You are an experienced DevOps engineer with a strong background in deploying and managing software applications in production environments. You have a deep understanding of deployment strategies, and you excel at ensuring that applications are deployed efficiently and securely.",
    verbose = True,
    allow_delegation = False,
    llm = llm
)


planning_task = Task(
    description = """
    Break down the following project idea into clear and strategic development steps:
    {project_idea}
    
    Include the following in your breakdown:
    1. Key deliverables
    2. Features 
    3. Required tools, technologies, and data sources
    """,
    expected_output = "A well-structured and detailed breakdown of the project idea into actionable development steps, including expected deliverables, features, tools, and technologies.",
    agent = planner_agent
)
developing_task = Task(
    description = """
    Based on the planner's breakdown, develop the software application by generating:
    1. Project Structure
    2. Source Code
    3. Configuration Files
    4. API Definitions
    5. Database Schema if required

    If the project can be built efficiently using simpler data sources, tools or technologies, prioritize those over more complex options. 
    If the user has provided specific requirements or constraints, ensure that the developed software application adheres to those. If not, use simple yet efficient tools, technologies, and data sources to build the application.
    """,
    expected_output = "A fully developed software application that meets the defined requirements with clean, modular and production-ready code.",
    agent = developer_agent
)
testing_task = Task(
    description = """
    Test the software application built by the developer to ensure it meets the defined requirements and quality standards. Identify:

    1. Potential bugs or issues 
    2. Edge Cases
    3. Performance Bottlenecks
    """,
    expected_output = "A comprehensive testing report that identifies any bugs, issues, edge cases and performance bottlenecks.",
    agent = tester_agent
)
reviewing_task = Task(
    description = """
    Based on the testing report and the developed software application, provide effective feedback on the software application. Focus on:
    
    1. Readability
    2. Maintainability
    3. Performance
    4. Security
    5. Best Practices
    """,
    expected_output = "Effective feedback on the software application, along with actionable suggestions for improving readability, maintainability, performance, security, and adherence to best practices.",
    agent = reviewer_agent
)
deploying_task = Task(
    description = """
    Based on the final version of the software application, generate a deployment plan for deploying the application to a production environment. The plan should include:
    
    1. Required Docker files for containerization
    2. CI/CD pipeline configuration for automated deployment
    3. Best practices for Secure and Scalable deployment

    DO NOT deploy the application yourself, just provide a detailed deployment plan and necessary configuration files.
    """,
    expected_output = "A comprehensive deployment plan that includes Docker, CI/CD pipeline configuration files and best practices for secure and scalable deployment.",
    agent = deployer_agent
)

def assemble_crew():
    tech_crew = Crew(
        agents=[planner_agent, developer_agent, tester_agent, reviewer_agent, deployer_agent],
        tasks=[planning_task, developing_task, testing_task, reviewing_task, deploying_task],
        process=Process.sequential
    )
    return tech_crew
