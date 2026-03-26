competitors = [
    {"rank": 1, "name": "Deloitte LS", "accounts": 9, "score": 74, "risk": "High"},
]

accounts = [
    {"name": "MedLife Systems", "incumbent": "Deloitte LS", "industry": "Healthcare", "value": "$2.8M", "score": 83},
]

# ─── Full 10-Slide + Rich Dashboard Mock ───────────────────────────────
mock_crewai_output = {
    "target_account": "MedLife Systems",
    "competitor_name": "Deloitte LS",
    "dashboard_metrics_package": {
        "displacement_score": {"value": 86, "benchmark": 54},
        "roi_projection": {"value": "$37.4M", "confidence": "96%"},
        "gap_analysis": [
            {"Gap_Area": "Data Engineering Velocity", "Current_State": "Slow/Batch Delivery", "Agilisium_Accelerator": "Real-time AI Pipeline", "Impact": "High"},
            {"Gap_Area": "Cloud Spend Efficiency", "Current_State": "High overhead", "Agilisium_Accelerator": "FinOps Framework", "Impact": "Critical"},
            {"Gap_Area": "AI Readiness", "Current_State": "Proof of Concepts only", "Agilisium_Accelerator": "Enterprise GenAI Hub", "Impact": "High"},
            {"Gap_Area": "Data Integrity & Quality", "Current_State": "Manual reconciliation", "Agilisium_Accelerator": "Data Vigor Platform", "Impact": "Critical"},
            {"Gap_Area": "Regulatory Compliance", "Current_State": "Manual GxP tracking", "Agilisium_Accelerator": "Automated Compliance Engine", "Impact": "Medium"},
        ],
        "market_benchmarks": [
            {"metric": "Data Integrity", "value": "62%", "industry_average": "88%", "gap": "-26%"},
            {"metric": "AI Adoption", "value": "12%", "industry_average": "45%", "gap": "-33%"},
            {"metric": "Cloud ROI", "value": "1.2x", "industry_average": "3.8x", "gap": "-68%"},
            {"metric": "Time-to-Insight", "value": "14 days", "industry_average": "2 days", "gap": "-86%"},
            {"metric": "Pipeline Uptime", "value": "94.2%", "industry_average": "99.5%", "gap": "-5.3%"},
        ],
        "financial_projections": {
            "year_1_savings": "$12.5M",
            "implementation_cost": "$4.1M",
            "payback_period": "4 Months",
            "cost_savings": {
                "infrastructure": "$3.2M",
                "operational": "$5.8M",
                "licensing": "$2.1M",
                "personnel_reallocation": "$1.4M",
            },
            "revenue_impact": {
                "accelerated_ttm": "$8.4M",
                "new_capabilities": "$4.2M",
                "competitive_wins": "$12.3M",
            },
        },
        "visualization_config": {"primary_color": "#C9A84C", "secondary": "#7B2D8B"},
        "executive_summary_metrics": {
            "Agilisium_Value": "88/100",
            "Risk_Avoidance": "$5.2M",
            "Innovation_Acceleration": "3.2x",
            "Competitive_Advantage": "Top Quartile",
            "Data_Maturity_Uplift": "+340%",
            "Agent_Confidence": "96%",
        },
    },
    "executive_powerpoint": [
        {
            "slide": 1,
            "title": "Current State Analysis",
            "subtitle": "Infrastructure Baseline",
            "headline": "Legacy systems creating 30% efficiency gap vs industry leaders",
            "content": "A comprehensive audit of MedLife Systems' current data infrastructure reveals critical dependencies on legacy ETL pipelines originally deployed in 2018. The organization processes approximately 2.4TB of clinical and operational data daily through batch workflows with an average latency of 14 hours. This represents a significant deviation from the industry benchmark of near-real-time processing. The current Deloitte LS engagement has maintained status quo rather than driving modernization.",
            "bullets": ["30% process bloat identified across 12 core pipelines", "Latency exceeds SLA by 4h on average", "Manual reconciliation required for 67% of data handoffs", "3 critical single-points-of-failure in production"],
            "visual_recommendations": "Infrastructure heatmap showing legacy vs modern pipeline performance",
            "speaker_notes": "Emphasize that the 30% bloat is confirmed by their recent internal report IR-2024. The 14-hour latency figure comes from their own monitoring dashboards.",
            "citations": ["Life Sciences Tech Monitor 2024", "Internal Audit Findings IR-2024", "Gartner Data Pipeline Benchmark Q3 2024"]
        },
        {
            "slide": 2,
            "title": "Industry Challenge Context",
            "subtitle": "Life Sciences Digital Imperative",
            "headline": "Market pressure demands 45% faster molecule-to-market timeline",
            "content": "The global Life Sciences industry is undergoing unprecedented digital transformation pressure. FDA approval timelines have compressed by 23% since 2020, while the cost of clinical data management has risen 34%. Organizations that fail to modernize their data infrastructure face existential competitive risk. MedLife Systems' current trajectory places them in the bottom quartile of digital readiness among peer organizations.",
            "bullets": ["FDA approval timelines compressed 23% since 2020", "Clinical data management costs up 34%", "Top-quartile performers achieve 3.8x better data ROI", "67% of LS executives cite data modernization as #1 priority"],
            "visual_recommendations": "Industry trend chart showing digital maturity vs competitive positioning",
            "speaker_notes": "Reference the Everest Group Life Sciences IT Services report for credibility. Highlight that 'do nothing' is actually the riskiest strategy.",
            "citations": ["Everest Group LS IT Services 2024", "McKinsey Digital Health Report", "FDA CDER Approval Statistics"]
        },
        {
            "slide": 3,
            "title": "Stale Incumbent Signals",
            "subtitle": "Competitor Performance Gaps",
            "headline": "Deloitte LS engagement showing 6 critical underperformance indicators",
            "content": "Analysis of the current Deloitte LS engagement reveals systematic underperformance across key delivery metrics. Project milestone adherence has dropped to 72% over the last 4 quarters, while scope creep has increased the original contract value by an estimated 28%. The delivery team has experienced 40% turnover, resulting in knowledge loss and repeated onboarding cycles. Most critically, the promised AI/ML capabilities remain at proof-of-concept stage after 18 months.",
            "bullets": ["72% milestone adherence (industry standard: 90%+)", "28% scope creep on original contract value", "40% delivery team turnover in 12 months", "AI/ML capabilities still at PoC after 18 months", "Zero production-grade automation delivered", "Client satisfaction score: 6.2/10 (below contract SLA of 8.0)"],
            "visual_recommendations": "Performance dashboard comparing Deloitte metrics vs contract SLAs",
            "speaker_notes": "Be diplomatic but factual. These numbers create urgency without being adversarial. Focus on impact to MedLife's business outcomes.",
            "citations": ["Contract Performance Review Q4 2024", "Industry Delivery Benchmark (ISG)", "Glassdoor/LinkedIn Team Analysis"]
        },
        {
            "slide": 4,
            "title": "Competitive Gap Analysis",
            "subtitle": "Technical & Strategic Limitations",
            "headline": "5 critical capability gaps identified across data, AI, and cloud domains",
            "content": "Our validated gap analysis reveals five interconnected capability deficits that compound to create a 30% operational premium on MedLife's current data operations. The gaps span data engineering velocity, cloud spend optimization, AI readiness, data quality management, and regulatory compliance automation. Each gap has been verified against industry benchmarks and mapped to quantifiable business impact.",
            "bullets": ["Data Engineering: 7x slower than industry benchmark", "Cloud Spend: $3.2M annual overspend vs optimized state", "AI Readiness: 0 production models vs industry median of 12", "Data Quality: 38% of records require manual intervention", "Compliance: 200+ hours/quarter spent on manual GxP tracking"],
            "visual_recommendations": "Gap analysis radar chart with 5 dimensions showing current vs target state",
            "speaker_notes": "Each gap directly maps to an Agilisium accelerator — set up the next slide's solution mapping. Emphasize the compounding effect.",
            "citations": ["Validated Gap Analysis Report", "Industry Benchmarks (Gartner, Everest Group)", "MedLife Internal Performance Data"]
        },
        {
            "slide": 5,
            "title": "Agilisium FDX Solution Overview",
            "subtitle": "NextGen DataOps Platform",
            "headline": "End-to-end displacement through 4 proprietary accelerators",
            "content": "Agilisium's NextGen DataOps Platform provides a comprehensive, integrated solution specifically designed for Life Sciences organizations. The FDX (Fast Data Exchange) architecture enables plug-and-play deployment that begins delivering value within weeks, not months. Our platform has been recognized by Everest Group as a 'Major Contender' in Life Sciences IT Services and by ISG as a 'Rising Star' in data engineering.",
            "bullets": ["GenInsights: Self-service analytics replacing static BI", "Data Vigor: Real-time data observability and monitoring", "Gene Inspector: Omics and genomics data unification", "Autonomous Agentic AI: Intelligent process automation"],
            "visual_recommendations": "Platform architecture diagram showing the 4 accelerators and integration points",
            "speaker_notes": "This is the transition slide from 'problem' to 'solution'. Emphasize the Everest Group and ISG recognition as proof points.",
            "citations": ["Everest Group PEAK Matrix 2024", "ISG Provider Lens 2024", "Agilisium Platform Documentation"]
        },
        {
            "slide": 6,
            "title": "Accelerator Portfolio Deep Dive",
            "subtitle": "Solution-to-Gap Mapping",
            "headline": "Point-by-point resolution for every identified capability gap",
            "content": "Each identified gap in MedLife's infrastructure maps directly to a proven Agilisium accelerator with documented success metrics from comparable Life Sciences deployments. GenInsights replaces batch reporting with real-time self-service analytics, reducing time-to-insight from 14 days to under 2 hours. Data Vigor provides continuous data quality monitoring, eliminating the 67% manual reconciliation burden. Gene Inspector unifies fragmented omics data across research silos.",
            "bullets": ["GenInsights → Data Engineering Velocity: 14 days → 2 hours", "Data Vigor → Data Quality: 62% → 95%+ automated integrity", "Gene Inspector → Regulatory Compliance: 200h → 20h per quarter", "Agentic AI → Cloud Optimization: $3.2M annual savings", "Plug & Play deployment: First value in 4 weeks"],
            "visual_recommendations": "Gap-to-solution mapping table with impact scores",
            "speaker_notes": "Walk through each mapping with confidence. These are proven outcomes from 15+ comparable deployments. Offer to share specific case studies on request.",
            "citations": ["Agilisium Case Study Library", "Client Deployment Metrics Database", "Platform Performance Benchmarks"]
        },
        {
            "slide": 7,
            "title": "Quantified Business Impact",
            "subtitle": "Disruption Score & ROI Projections",
            "headline": "$37.4M Total ROI with 96% confidence over 36 months",
            "content": "Our market-based displacement analysis yields a Displacement Score of 86/100, placing MedLife Systems in the 'High Displacement Opportunity' category. Financial modeling based on verified industry benchmarks projects $37.4M in total ROI over 36 months, with a conservative 96% confidence interval. Year 1 alone delivers $12.5M in savings against an implementation investment of $4.1M, achieving full payback within 4 months.",
            "bullets": ["Displacement Score: 86/100 (Top 5% of assessments)", "Total ROI: $37.4M over 36 months", "Year 1 Savings: $12.5M (3x implementation cost)", "Payback Period: 4 months", "Risk Avoidance Value: $5.2M", "Innovation Acceleration: 3.2x improvement"],
            "visual_recommendations": "ROI waterfall chart and displacement score gauge",
            "speaker_notes": "The $37.4M is derived from conservative industry benchmarks. Present this as a 'floor estimate' — actual returns from comparable deployments have exceeded projections by 15-20%.",
            "citations": ["IDC Cloud ROI Study 2024", "Agilisium Deployment Analytics", "Displacement Methodology v3.0"]
        },
        {
            "slide": 8,
            "title": "Accelerating Scientific Innovation",
            "subtitle": "Molecule-to-Market Impact",
            "headline": "45% reduction in molecule-to-market timeline through data modernization",
            "content": "The ultimate value proposition extends beyond operational efficiency. By modernizing MedLife's data infrastructure, Agilisium directly accelerates the molecule-to-market pipeline. Real-time data availability enables faster research iterations, automated compliance reduces regulatory bottlenecks, and predictive analytics identifies promising candidates earlier in the development cycle. This translates to an estimated $8.4M in accelerated time-to-market revenue.",
            "bullets": ["Research iteration cycles reduced from weeks to days", "Regulatory submission prep time cut by 75%", "Predictive candidate identification: 2.8x improvement", "Cross-functional data sharing: real-time vs quarterly", "Clinical trial data processing: 14 days → 4 hours"],
            "visual_recommendations": "Timeline comparison showing current vs optimized molecule-to-market journey",
            "speaker_notes": "This slide connects the technical solution to the C-suite's ultimate concern: getting products to market faster. Tie this back to the competitive pressure from Slide 2.",
            "citations": ["Tufts CSDD Drug Development Studies", "FDA Digital Health Innovation Plan", "Agilisium LS Case Studies"]
        },
        {
            "slide": 9,
            "title": "Implementation Roadmap",
            "subtitle": "Phased Deployment Strategy",
            "headline": "12-month phased deployment with value delivery starting Month 1",
            "content": "The implementation follows a proven 3-phase approach designed to deliver incremental value while minimizing operational disruption. Phase 1 (Months 1-2) establishes the foundational architecture and deploys Data Vigor for immediate data quality improvements. Phase 2 (Months 3-6) migrates core pipelines and launches GenInsights for self-service analytics. Phase 3 (Months 7-12) activates advanced AI capabilities, Gene Inspector, and full automation.",
            "bullets": ["Phase 1 (M1-2): Architecture & Data Vigor — immediate quality wins", "Phase 2 (M3-6): Pipeline migration & GenInsights — analytics transformation", "Phase 3 (M7-12): AI activation & Gene Inspector — full capability", "Zero-downtime migration with parallel run validation", "Dedicated Agilisium deployment squad of 12 specialists"],
            "visual_recommendations": "Gantt-style timeline with phased milestones and value delivery markers",
            "speaker_notes": "Emphasize the 'value from Day 1' approach. Phase 1 deliverables alone justify the engagement start. Each phase has defined success metrics and go/no-go gates.",
            "citations": ["Agilisium Deployment Methodology v5", "Change Management Best Practices (Prosci)", "Similar Client Deployment Timelines"]
        },
        {
            "slide": 10,
            "title": "Executive Decision Framework",
            "subtitle": "Risk Mitigation & Next Steps",
            "headline": "92% historical success rate across 40+ comparable deployments",
            "content": "This executive decision framework provides the strategic rationale, risk assessment, and recommended next steps for proceeding with the displacement engagement. Based on 40+ comparable deployments in Life Sciences, Agilisium has achieved a 92% success rate in meeting or exceeding projected outcomes. The recommended next step is a 2-week Discovery Workshop to validate findings and finalize the deployment plan.",
            "bullets": ["Success probability: 92% based on 40+ comparable deployments", "Risk mitigation: Phased approach with exit gates at each milestone", "Governance: Bi-weekly steering committee with executive sponsors", "SLA guarantees: Performance-linked contract terms", "Next step: 2-week Discovery Workshop (no commitment required)"],
            "visual_recommendations": "Decision matrix with risk/reward quadrants and recommendation highlight",
            "speaker_notes": "Close with confidence but not pressure. The Discovery Workshop is a low-commitment next step that demonstrates value. Offer to customize the workshop agenda based on their priorities.",
            "citations": ["Agilisium Client Success Database", "Risk Management Framework", "Discovery Workshop Template v3"]
        },
    ],
    "formal_pdf_document": {
        "table_of_contents": "1. Executive Summary ........................ p.1\n2. Target Account Profile ................... p.3\n3. Competitive Gap Assessment ............... p.5\n4. Solution Portfolio & Mapping ............. p.7\n5. Business Case & ROI ...................... p.9\n6. Implementation Roadmap ................... p.10\n7. Methodology & Appendices ................. p.11",
        "executive_summary": "This Intelligence Report presents a comprehensive competitive displacement strategy for MedLife Systems, currently engaged with Deloitte LS across data engineering, analytics, and cloud infrastructure domains.\n\nOur verified intelligence analysis reveals significant underperformance in the incumbent engagement, with milestone adherence at 72% (vs 90%+ industry standard), 28% scope creep, and 40% delivery team turnover. Most critically, promised AI/ML capabilities remain at proof-of-concept stage after 18 months.\n\nThe Displacement Score of 86/100 indicates a prime opportunity for strategic displacement. Our analysis projects $37.4M in total ROI over 36 months, with Year 1 savings of $12.5M against an implementation investment of $4.1M — achieving full payback within 4 months.\n\nAgilisium's NextGen DataOps Platform, featuring GenInsights, Data Vigor, Gene Inspector, and Autonomous Agentic AI, provides a comprehensive solution mapped to every identified capability gap. With a 92% historical success rate across 40+ comparable LS deployments, the risk profile is firmly in the 'favorable' category.\n\nWe recommend an immediate 2-week Discovery Workshop to validate findings and finalize the deployment roadmap.",
        "detailed_findings": "INFRASTRUCTURE ASSESSMENT\nMedLife Systems processes approximately 2.4TB of clinical and operational data daily through legacy batch ETL pipelines deployed in 2018. Average processing latency is 14 hours, compared to the industry benchmark of near-real-time.\n\nKEY FINDINGS:\n• Data Engineering Velocity: 7x slower than industry benchmark\n• Cloud Spend: $3.2M annual overspend vs optimized state\n• AI Readiness: Zero production ML models (industry median: 12)\n• Data Quality: 38% of records require manual intervention\n• Regulatory Compliance: 200+ hours/quarter on manual GxP tracking\n\nINCUMBENT PERFORMANCE:\n• Milestone adherence: 72% (SLA target: 90%+)\n• Contract scope creep: 28% over original value\n• Team turnover: 40% in 12 months\n• Client satisfaction: 6.2/10 (SLA: 8.0/10)\n• AI delivery: PoC only after 18 months engagement",
        "solution_mapping": "GAP-TO-SOLUTION MAPPING:\n\n1. Data Engineering Velocity → GenInsights Platform\n   Replaces batch reporting with real-time self-service analytics.\n   Impact: Time-to-insight from 14 days → under 2 hours.\n\n2. Data Quality & Integrity → Data Vigor\n   Continuous automated data quality monitoring and remediation.\n   Impact: Manual reconciliation reduced from 67% → under 5%.\n\n3. Regulatory Compliance → Automated Compliance Engine\n   Eliminates manual GxP tracking with continuous monitoring.\n   Impact: 200 hours/quarter → 20 hours/quarter.\n\n4. Cloud Spend Efficiency → FinOps + Agentic AI\n   Intelligent workload optimization and cost management.\n   Impact: $3.2M annual savings on cloud infrastructure.\n\n5. Genomics & Research Data → Gene Inspector\n   Unified omics data platform accelerating research discovery.\n   Impact: Cross-silo analysis time reduced by 85%.",
        "implementation_roadmap": "PHASED DEPLOYMENT STRATEGY (12 Months)\n\nPHASE 1: Foundation (Months 1-2)\n• Architecture assessment and design\n• Data Vigor deployment for immediate quality wins\n• Parallel run environment setup\n• Quick wins: Data quality dashboard, monitoring alerts\n\nPHASE 2: Core Migration (Months 3-6)\n• Legacy pipeline migration to cloud-native\n• GenInsights platform launch\n• Self-service analytics enablement\n• User training and adoption program\n\nPHASE 3: Advanced Capabilities (Months 7-12)\n• Autonomous Agentic AI activation\n• Gene Inspector deployment for research teams\n• Full automation of compliance workflows\n• Performance optimization and scaling\n\nGOVERNANCE:\n• Bi-weekly steering committee meetings\n• Monthly executive sponsor reviews\n• Phase gate approvals with documented success criteria\n• Dedicated Agilisium squad: 12 specialists",
        "methodology": "ANALYSIS METHODOLOGY:\n\nData Sources: 40+ industry data points from Everest Group, ISG, Gartner, McKinsey, and FDA public databases. Direct telemetry analysis where access was provided.\n\nDisplacement Scoring: Standardized Displacement Methodology (v3.5) combining:\n• Legacy Infrastructure Impact (40% weight)\n• Market Readiness Assessment (30% weight)\n• Competitive Advantage Potential (30% weight)\n\nROI Calculations: Industry benchmark-based projections using verified case study outcomes from 15+ comparable LS deployments. Conservative estimates with 96% confidence interval.\n\nValidation: All claims cross-referenced against minimum 2 independent sources. Confidence levels assigned to each data point. Unverifiable claims explicitly flagged.",
        "appendices": "APPENDIX A: Full Metric Comparison Tables\n• 23 KPIs across 5 capability domains\n• Benchmark data from 8 peer organizations\n• Year-over-year trend analysis (3 years)\n\nAPPENDIX B: Vendor Comparison Matrix\n• Feature-by-feature comparison across 6 vendors\n• TCO analysis over 36-month horizon\n• Client satisfaction and NPS scores\n\nAPPENDIX C: Case Study Summaries\n• 5 comparable LS deployments with outcome data\n• Implementation timeline comparisons\n• Lessons learned and best practices\n\nAPPENDIX D: Technical Architecture Diagrams\n• Current state architecture\n• Proposed future state architecture\n• Migration pathway and integration points"
    },
    "export_specifications": {
        "formats": ["PDF", "PPTX", "JSON (API)", "CSV (Dashboard)", "Markdown"],
        "integration_instructions": "API webhooks ready for direct Salesforce / HubSpot integration. OAuth2 authentication supported. Real-time sync available for dashboard KPIs. Batch export scheduling for weekly leadership reports.",
        "qa_verification": "All outputs verified by Intelligence Specialist Agent. Cross-format consistency check passed. Financial metrics aligned across all 5 export formats. Citation integrity verified."
    },
    "implementation_package": {
        "cross_format_consistency": "Verified: All financial metrics ($37.4M ROI, $12.5M Y1 Savings, 4-month payback) are consistent across the Executive Summary, Dashboard JSON, PowerPoint deck, and PDF report. Displacement Score (86/100) confirmed in all formats.",
        "usage_recommendations": "• Dashboard Metrics: Share with Solution Engineers for real-time tracking\n• Executive Slides: Present to CIO/CTO during displacement pitch\n• PDF Report: Distribute to procurement and legal teams\n• API Export: Feed into CRM for opportunity tracking\n• Discovery Workshop: Use slides 1-4 for problem framing, 5-10 for solution pitch",
        "next_steps": "1. Schedule 2-week Discovery Workshop with MedLife Systems\n2. Prepare customized demo environment with sample data\n3. Identify internal champions: VP Data Engineering, CTO, CDO\n4. Draft Statement of Work based on Phase 1 scope\n5. Prepare ROI validation framework for client review"
    }
}
