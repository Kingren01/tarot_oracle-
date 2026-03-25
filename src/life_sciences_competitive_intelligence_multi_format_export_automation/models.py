from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class DisplacementScore(BaseModel):
    value: float
    benchmark: float

class ROIProjection(BaseModel):
    value: str
    confidence: str

class GapAnalysis(BaseModel):
    Gap_Area: str
    Current_State: str
    Agilisium_Accelerator: str
    Impact: str

class MarketBenchmark(BaseModel):
    metric: str
    value: str
    industry_average: str
    gap: str

class FinancialProjections(BaseModel):
    year_1_savings: str
    implementation_cost: str
    payback_period: str
    cost_savings: Optional[Dict[str, Any]] = None
    revenue_impact: Optional[Dict[str, Any]] = None

class DashboardMetricsPackage(BaseModel):
    displacement_score: DisplacementScore
    roi_projection: ROIProjection
    gap_analysis: List[GapAnalysis]
    financial_projections: FinancialProjections
    market_benchmarks: Optional[List[MarketBenchmark]] = None
    visualization_config: Dict[str, Any]
    executive_summary_metrics: Optional[Dict[str, Any]] = None

class Slide(BaseModel):
    slide: int
    title: str
    subtitle: Optional[str] = None
    headline: Optional[str] = None
    content: str
    bullets: Optional[List[str]] = None
    visual_recommendations: Optional[str] = None
    speaker_notes: Optional[str] = None
    citations: Optional[List[str]] = None

class FormalPDFDocument(BaseModel):
    table_of_contents: Optional[str] = None
    executive_summary: str
    detailed_findings: str
    solution_mapping: str
    implementation_roadmap: str
    methodology: Optional[str] = None
    appendices: Optional[str] = None
    source_count: Optional[int] = None

class ExportSpecifications(BaseModel):
    formats: List[str]
    integration_instructions: str
    qa_verification: str

class ImplementationPackage(BaseModel):
    cross_format_consistency: str
    usage_recommendations: str
    next_steps: str

class MasterExportPackage(BaseModel):
    target_account: str
    competitor_name: str
    dashboard_metrics_package: DashboardMetricsPackage
    executive_powerpoint: List[Slide]
    formal_pdf_document: FormalPDFDocument
    export_specifications: ExportSpecifications
    implementation_package: ImplementationPackage
