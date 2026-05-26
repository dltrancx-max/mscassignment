# Developing a Data Management Strategy for Eta-Beta-Pi

## 1. Executive Summary

This paper recommends a phased, hybrid data warehouse implementation strategy for Eta-Beta-Pi that balances practical franchise requirements, legacy transaction systems, and the need for centralized analytics. The strategy combines a centralized data warehouse with a distributed data ingestion architecture, using an enterprise data lake for raw franchise and PoS data and a dimensional data warehouse for reporting and analysis. The approach is designed to support OSIC's revitalisation goals by enabling timely insight into sales, inventory, margins, and franchise performance while accommodating diverse Point-of-Sale (PoS) systems and existing franchise reporting practices.

## 2. Introduction

Eta-Beta-Pi is a multinational fast-food franchise network with a long operating history and large variation in technology adoption across outlets. Current information collection relies mainly on monthly franchise reports and fragmented PoS data, with limited analysis of operating cost data and inconsistent back-office systems. OSIC wants a modern data management strategy to centralize information, improve decision-making, and support a retro dining repositioning of the brand.

This paper evaluates the practical and theoretical foundations of a data warehouse implementation for Eta-Beta-Pi and recommends a strategy that can be delivered quickly while allowing future growth.

## 3. Business Context and Requirements

### 3.1 Franchising Considerations

- Franchisees own and operate outlets independently while paying fees and obeying franchiser guidelines.
- Franchisees value some level of system autonomy for back-office operations to control costs and select local vendors.
- Franchise agreements may limit Eta-Beta-Pi's ability to mandate a single PoS solution or to directly access franchisee-owned data systems.
- Regulatory and tax compliance requirements vary by region, especially across multinational operations.
- Performance measurement must respect franchisee confidentiality while delivering aggregated insights to OSIC and Eta-Beta-Pi leadership.

### 3.2 Current Eta-Beta-Pi Situation

- API systems are outdated and there is low standardization across outlets.
- Monthly reports are the primary source of consolidated data, resulting in stale decisions and slow response to market changes.
- PoS systems vary by age and capability, producing inconsistent data schemas and quality.
- Operating cost and tax data remains largely outside central analysis, limiting profitability understanding.
- Margins information exists with Eta-Beta-Pi, suggesting some finance integration is already possible.

### 3.3 Key Stakeholder Needs

- Executive leadership requires accurate, near-real-time visibility into sales, margins, promotions, and outlet performance.
- Menu and product teams need rapid feedback on product adoption and campaign effectiveness.
- Franchise operations must be able to maintain autonomy while contributing necessary data.
- Finance teams require consolidated cost, margin, and revenue metrics.
- IT and analytics teams need a stable, scalable platform that can evolve as the brand and systems modernize.

## 4. Data Warehouse Strategy Options

### 4.1 Centralized Data Warehouse

A single centralized data warehouse collects, integrates, and stores data from all outlets and systems. This provides strong governance and consistent reporting, but can be challenging in a franchise context where not all partners can or want to expose raw operational data.

Pros:
- Single source of truth.
- Easier data governance and security enforcement.
- Strong analytical performance.

Cons:
- High initial integration effort across heterogeneous PoS systems.
- Franchise resistance if systems access is mandated.
- Upfront cost and time to build.

### 4.2 Federated Data Warehouse

A federated approach leaves data in local franchise systems and queries it virtually. It preserves autonomy but makes performance and data quality inconsistent.

Pros:
- Minimal disruption to franchisee systems.
- Faster initial deployment for reporting on available data.

Cons:
- Poor performance for complex analytics.
- Harder to enforce consistent definitions.
- Limited ability to handle legacy PoS systems and stale monthly reports.

### 4.3 Hub-and-Spoke / Hybrid Architecture

A hybrid strategy uses distributed data ingestion and centralized analytics. Franchisees continue using existing systems, but a central hub ingests cleansed data periodically, optionally via a data lake.

Pros:
- Supports phased delivery.
- Balances autonomy with central insight.
- Can integrate both modern and legacy data sources.

Cons:
- Still requires some coordination for staging and ETL.
- Needs investment in integration and metadata management.

### 4.4 Incremental/Agile Data Warehouse Implementation

This strategy prioritizes value delivery through small, iterative releases: start with a core warehouse for sales and margin analysis, then expand to inventory, operations, and franchise costs.

Pros:
- Rapid business value.
- Manageable risk.
- Easier change management for franchisees.

Cons:
- Requires strong product and project management discipline.
- Delivers limited scope initially.

## 5. Recommended Strategy for Eta-Beta-Pi

### 5.1 Proposed Approach: Phased Hybrid Data Warehouse

The best strategy for Eta-Beta-Pi is a phased hybrid implementation with these main elements:

1. Establish a central data warehouse and data lake in the cloud or on-premises depending on OSIC’s infrastructure preferences.
2. Use a data lake to ingest raw franchise and PoS data from multiple sources, preserving original records.
3. Build a dimensional data warehouse for consistent reporting on sales, margins, outlets, products, and promotions.
4. Implement an Extract-Load-Transform (ELT) pipeline for modern flexibility, with transformation logic applied inside the data warehouse.
5. Roll out initial reporting for core finance and operations metrics, then expand to franchise-level operating cost analysis and eventually predictive capacity.

### 5.2 Justification

- The hybrid architecture respects franchise autonomy by not forcing all outlets into a single PoS system.
- A data lake allows capturing raw data from diverse systems, including monthly reports, interoperable PoS exports, and eventual franchise ERP or payroll feeds.
- A central dimensional warehouse delivers consistent analytics and supports OSIC’s decision-making needs.
- A phased delivery lowers risk and helps demonstrate value quickly, which is critical for OSIC’s revitalization agenda.

### 5.3 Target Architecture

- Source systems: legacy PoS systems, monthly franchise reports, finance/margin spreadsheets, supplier and inventory systems, HR/payroll systems if available.
- Ingestion layer: API, file upload, secure FTP, or manual upload portals for franchises with older systems.
- Data lake: staged raw data storage (structured, semi-structured) with security zones.
- Data warehouse: dimensional model with fact tables for sales, margins, inventory usage, promotions, and franchise performance.
- Analytics/reporting: BI dashboards, self-service analytics, and prebuilt executive reports.

## 6. Practical Issues and Implementation Considerations

### 6.1 Source Data Collection and Loading

#### 6.1.1 Handling Diverse PoS Systems

- Conduct an initial data source inventory and classify outlets by technology tier.
- For modern PoS systems, use APIs or scheduled data exports to ingest transactions and item-level sales.
- For legacy systems, use file-based extracts (CSV/Excel) or middleware connectors to collect standardized summaries.
- Provide franchisees with templates and validation tools to improve data quality from older systems.

#### 6.1.2 Monthly Report Integration

- Continue using monthly reports initially, but standardize the report format and automate loading.
- Implement a secure upload portal or franchise portal where monthly reports are submitted in a standardized template.
- Use the data lake to stage these reports and ETL routines to transform them into warehouse records.

#### 6.1.3 Franchisee Operating Data

- Encourage franchisees to share operating cost and tax data in a standard template or via secure file exchange.
- Initially ingest broad cost categories rather than detailed payroll records, to reduce resistance and protect privacy.
- Use data governance policies to define which operating data is required, optional, and aggregated for reporting.

### 6.2 Data Quality, Governance, and Integration

- Define a data governance framework covering data ownership, definitions, quality checks, and access rights.
- Establish standard dimensions for outlets, products, time periods, promotions, and franchisees.
- Implement data profiling and validation during ingestion to flag missing or inconsistent data.
- Create a metadata catalog so analysts can understand data lineage from source to report.

### 6.3 Security and Compliance

- Secure data in transit and at rest using encryption and access controls.
- Apply role-based access controls to ensure franchisees only see their own outlet data while headquarters analysts can view aggregated results.
- Consider legal and privacy requirements in each country of operation, especially for employee-related cost data.
- Use anonymization or aggregation where necessary to protect sensitive franchisee data.

### 6.4 Change Management and Franchise Adoption

- Build trust through transparency: clearly communicate the benefits of the central analytics platform to franchisees.
- Provide training, documentation, and support for standardized data submission processes.
- Offer phased onboarding so a subset of outlets can pilot the system before full rollout.
- Preserve franchise flexibility by not requiring immediate migration of legacy PoS systems.

### 6.5 Technology Selection

- Prefer cloud-native data warehouse and data lake offerings if OSIC is open to cloud deployment, as they simplify scaling and modernization.
- If cloud is not feasible, choose a flexible enterprise data warehouse platform that supports ELT and modern connectivity.
- Include a low-code ETL/ELT tool or data integration platform that supports API, file, and database ingestion.
- Ensure the BI layer can support both executive dashboards and franchisee-specific views.

## 7. Data Model and Reporting Strategy

### 7.1 Dimensional Model

Key warehouse components should include:

- FactSales: item-level or transaction-level sales, units sold, revenue, discounts, and outlet-level details.
- FactMargin: outlet margin metrics, cost of goods sold, gross margin, net margin, and profitability by outlet.
- FactInventory: stock levels, usage, waste, purchase costs, and supplier relationships.
- FactFranchiseCosts: franchisee operating expenses, labor cost categories, taxes, and overhead.
- DimOutlet: location, franchisee, format, brand concept, opening date, and region.
- DimProduct: menu item, category, cost, recommended price, and menu attribution.
- DimTime: daily/weekly/monthly period definitions for trend analysis.
- DimPromotion: promotion campaigns, offer details, start/end dates, and associated outlets.

### 7.2 Reporting and Analytics

Initial reports should address:

- Sales and revenue trends by outlet, region, menu category, and product.
- Margin performance and profitability by outlet and product.
- Product adoption and menu item performance for new or retro offerings.
- Franchisee compliance with reporting requirements and data submission timeliness.
- Inventory performance, waste, and purchase cost trends.
- Cost structure analysis by franchisee and outlet.

## 8. Implementation Roadmap

### Phase 1: Discovery and Foundation

- Conduct a detailed source system inventory and stakeholder analysis.
- Define business requirements and key performance indicators.
- Design the data architecture, security model, and metadata framework.
- Build the data lake and warehouse foundation with core dimensions.
- Pilot ingestion from a subset of modern PoS systems and monthly report templates.

### Phase 2: Core Data Warehouse Deployment

- Implement the dimensional model for sales, margins, and outlet dimensions.
- Develop ETL/ELT pipelines for core data sources.
- Deploy initial dashboards for executive, finance, and operations teams.
- Begin onboarding early pilot outlets and validate data quality.

### Phase 3: Franchise and Operating Cost Integration

- Expand ingestion to franchise operating costs, tax data, and legacy PoS extracts.
- Enhance governance, data quality monitoring, and metadata documentation.
- Add additional reporting for franchise profitability and cost structure.
- Provide training and onboarding to more franchisees.

### Phase 4: Advanced Analytics and Continuous Improvement

- Introduce predictive analytics for demand forecasting, menu optimization, and outlet performance.
- Integrate supplier, inventory, and labor planning data.
- Refine dashboards and self-service analytics capabilities.
- Establish continuous data governance and improvement processes.

## 9. Theoretical Considerations

### 9.1 Data Warehouse Principles

- Subject-oriented: The warehouse should focus on key business areas such as sales, margins, and franchise performance.
- Integrated: Data from multiple PoS systems and reports must be harmonized.
- Time-variant: Analyses should support trends over time, which is essential for menu and marketing decisions.
- Non-volatile: Once loaded, historical data should remain stable for reliable reporting.

### 9.2 Model Selection

- A dimensional model is preferred for usability and performance in BI reporting.
- The data lake supports raw and semi-structured inputs, allowing flexibility for future changes.
- ELT is recommended over ETL because modern warehouses are optimized for in-database transformations and the raw data landing zone preserves source detail.

### 9.3 Scalability and Maintainability

- The architecture must scale from hundreds to potentially more outlets over time.
- Modular pipelines and metadata-driven transformations make the solution easier to maintain.
- A central governance program ensures consistency across data domains.

## 10. Risks and Mitigations

- Data quality risk: Mitigate with standard templates, validation, and pilot onboarding.
- Franchise resistance: Mitigate by preserving autonomy and focusing on benefits and confidentiality.
- Legacy system complexity: Mitigate with flexible ingestion paths and a data lake for raw staging.
- Cost and delivery risk: Mitigate with a phased, value-driven implementation and strong project governance.

## 11. Conclusion

A phased hybrid data warehouse strategy is the best fit for Eta-Beta-Pi. It can deliver modern analytics quickly while accommodating diverse franchise technology and legacy PoS systems. By combining a data lake for raw data collection with a dimensional warehouse for reporting, OSIC can create a scalable foundation that supports revitalizing the brand and making better business decisions.

## 12. References

- Inmon, W. H. (2005). Building the Data Warehouse. John Wiley & Sons.
- Kimball, R., & Ross, M. (2013). The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling. John Wiley & Sons.
- Golfarelli, M., & Rizzi, S. (2009). Data Warehouse Design: Modern Principles and Methodologies. McGraw-Hill.
- Loshin, D. (2012). Business Intelligence: The Savvy Manager's Guide. Morgan Kaufmann.
