import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool,
	ScrapeWebsiteTool,
	FileReadTool
)

# Import the data model for structured output
from life_sciences_competitive_intelligence_multi_format_export_automation.models import MasterExportPackage

@CrewBase
class LifeSciencesCompetitiveIntelligenceMultiFormatExportAutomationCrew:
    """LifeSciencesCompetitiveIntelligenceMultiFormatExportAutomation crew"""
    
    # Define models consistently for all agents
    # Use OpenRouter for gpt-4o as configured in our environment
    standard_llm = "openrouter/openai/gpt-4o"
    mini_llm = "openrouter/openai/gpt-4o-mini"
    
    @agent
    def life_sciences_intelligence_data_verification_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["life_sciences_intelligence_data_verification_specialist"], # type: ignore[index]
            tools=[SerperDevTool(), ScrapeWebsiteTool(), FileReadTool()],
            verbose=True,
            llm=self.standard_llm,
        )
    
    @agent
    def verified_gap_analysis_pain_point_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["verified_gap_analysis_pain_point_specialist"], # type: ignore[index]
            tools=[SerperDevTool()],
            verbose=True,
            llm=self.standard_llm,
        )
    
    @agent
    def principal_solutions_architect_life_sciences_data_innovation(self) -> Agent:
        return Agent(
            config=self.agents_config["principal_solutions_architect_life_sciences_data_innovation"], # type: ignore[index]
            tools=[ScrapeWebsiteTool()],
            verbose=True,
            llm=self.standard_llm,
        )
    
    @agent
    def executive_communications_architect_fdx_standard(self) -> Agent:
        return Agent(
            config=self.agents_config["executive_communications_architect_fdx_standard"], # type: ignore[index]
            tools=[],
            verbose=True,
            llm=self.standard_llm,
        )
    
    @agent
    def quantitative_data_analyst_market_benchmark_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["quantitative_data_analyst_market_benchmark_specialist"], # type: ignore[index]
            tools=[SerperDevTool()],
            verbose=True,
            llm=self.standard_llm,
        )
    
    @agent
    def data_export_formatting_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["data_export_formatting_specialist"], # type: ignore[index]
            tools=[],
            verbose=True,
            llm=self.mini_llm,
        )
    
    @agent
    def dashboard_metrics_kpi_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["dashboard_metrics_kpi_generator"], # type: ignore[index]
            tools=[],
            verbose=True,
            llm=self.mini_llm,
        )
    
    @task
    def verified_intelligence_research_target_account_competitor_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["verified_intelligence_research_target_account_competitor_analysis"], # type: ignore[index]
        )
    
    @task
    def validated_gap_analysis_infrastructure_service_delivery_assessment(self) -> Task:
        return Task(
            config=self.tasks_config["validated_gap_analysis_infrastructure_service_delivery_assessment"], # type: ignore[index]
        )
    
    @task
    def apply_the_agilisium_angle_map_proprietary_accelerators(self) -> Task:
        return Task(
            config=self.tasks_config["apply_the_agilisium_angle_map_proprietary_accelerators"], # type: ignore[index]
        )
    
    @task
    def market_based_roi_calculation_displacement_scoring(self) -> Task:
        return Task(
            config=self.tasks_config["market_based_roi_calculation_displacement_scoring"], # type: ignore[index]
        )
    
    @task
    def generate_executive_displacement_strategy_10_slide_format(self) -> Task:
        return Task(
            config=self.tasks_config["generate_executive_displacement_strategy_10_slide_format"], # type: ignore[index]
        )
    
    @task
    def generate_comprehensive_10_page_executive_summary(self) -> Task:
        return Task(
            config=self.tasks_config["generate_comprehensive_10_page_executive_summary"], # type: ignore[index]
        )
    
    @task
    def generate_dashboard_metrics_kpis(self) -> Task:
        return Task(
            config=self.tasks_config["generate_dashboard_metrics_kpis"], # type: ignore[index]
        )
    
    @task
    def create_slide_deck_export_package(self) -> Task:
        return Task(
            config=self.tasks_config["create_slide_deck_export_package"], # type: ignore[index]
        )
    
    @task
    def master_export_package_compilation(self) -> Task:
        return Task(
            config=self.tasks_config["master_export_package_compilation"], # type: ignore[index]
            output_pydantic=MasterExportPackage
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            # chat_llm=self.mini_llm,
        )
