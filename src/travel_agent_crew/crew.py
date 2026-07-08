from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import SerperDevTool


@CrewBase
class travel_agent_crew():
    """Trip Planner Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # -------------------------------
    # Tools
    # -------------------------------

    search_tool = SerperDevTool()



    # -------------------------------
    # Agents
    # -------------------------------

    @agent
    def city_finder(self) -> Agent:
        return Agent(
            config=self.agents_config["city_finder"],
            tools=[self.search_tool],
            verbose=True,
        )

    @agent
    def place_finder(self) -> Agent:
        return Agent(
            config=self.agents_config["place_finder"],
            tools=[self.search_tool],
            verbose=True,
        )

    @agent
    def hotel_finder(self) -> Agent:
        return Agent(
            config=self.agents_config["hotel_finder"],
            tools=[self.search_tool],
            verbose=True,
        )

    @agent
    def planner(self):
        return Agent(
            config=self.agents_config["planner"],
            verbose=True
        )

    # -------------------------------
    # Tasks
    # -------------------------------

    @task
    def best_city_task(self) -> Task:
        return Task(
            config=self.tasks_config["best_city_task"],
        )

    @task
    def best_place_task(self) -> Task:
        return Task(
            config=self.tasks_config["best_place_task"],
        )

    @task
    def best_hotel_task(self) -> Task:
        return Task(
            config=self.tasks_config["best_hotel_task"],
        )

    @task
    def plan_task(self) -> Task:
        return Task(
            config=self.tasks_config["plan_task"],
        )

    # -------------------------------
    # Crew
    # -------------------------------

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )