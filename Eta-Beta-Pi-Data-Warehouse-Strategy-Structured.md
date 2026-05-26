# Developing a Data Management Strategy for Eta-Beta-Pi

## Abstract

This paper presents a data warehouse implementation strategy for Eta-Beta-Pi, a legacy fast-food franchise undergoing revitalization by OSIC. It proposes a phased, hybrid architecture that centralizes analytics while accommodating diverse Point-of-Sale systems and franchise autonomy. The strategy emphasizes practical data loading, governance, and a strong enterprise foundation.

## Introduction

Eta-Beta-Pi is a multinational fast-food franchise with a long history and heterogeneous back-office systems. The current reporting process relies on monthly franchise submissions and fragmented PoS data. OSIC seeks a modern information system that supports faster, data-driven decisions for menu changes, promotions, and financial performance.

## Business Case

Eta-Beta-Pi needs a centralized data platform to reverse declining market share and support OSIC’s retro dining repositioning. The business case includes:
- Improving visibility into outlet sales, margins, and promotions.
- Standardizing data from multiple franchise systems.
- Enabling faster response to customer and market trends.
- Supporting profitable franchise performance and cost management.
- Reducing reliance on stale monthly reports.

## Literature Review

Data warehouse theory establishes that successful analytics depend on integrated, subject-oriented, time-variant, and non-volatile data storage. Core references include Kimball and Ross for dimensional modeling and Inmon for enterprise warehouse design. Modern practices favor ELT and data lakes as flexible landing zones for heterogeneous sources. In franchise contexts, hybrid architectures and phased deployments are widely recommended to balance central control with local autonomy.

## User Stories / Use Cases

### User Stories

- As a franchise operations manager, I want to compare outlet performance by region so I can support struggling locations.
- As a finance analyst, I want consolidated margin reports so I can identify low-profit menu items.
- As a marketing lead, I want near-real-time sales trends so I can evaluate promotional campaigns.
- As a franchise owner, I want secure access to only my outlet data so I can review my business performance.
- As an IT director, I want a scalable data platform so I can integrate new PoS systems over time.

### Use Cases

1. Monthly franchise report ingestion and validation.
2. Sales and margin analysis across outlets and product categories.
3. Inventory and waste trend reporting for supply chain decisions.
4. Franchisee operating cost analysis for profitability planning.
5. Product adoption tracking for new retro menu launches.

## Enterprise Approach for the Solution

The enterprise approach prioritizes a central analytics hub supported by a data ingestion layer and strong governance. Key aspects:
- Use a data lake to ingest raw and semi-structured data from PoS systems, franchise reports, and finance feeds.
- Build a dimensional data warehouse for reporting and analysis across key business domains.
- Maintain metadata, data quality checks, and role-based access control.
- Adopt a phased rollout to pilot early and expand gradually.
- Preserve franchise autonomy by supporting multiple ingestion methods and not forcing a single PoS system.

## Proposed Solution

The proposed solution is a hybrid data warehouse with the following elements:
- A central data lake for raw transaction, report, and cost data.
- A dimensional warehouse with fact tables for sales, margins, inventory, and costs.
- ELT-based pipelines to transform stage data into analytical models.
- BI dashboards for executives, finance, marketing, and franchisees.
- A secure ingestion portal for monthly report submissions.

## Critical Analysis with Solution Justification

### Analysis

- Centralized analytics deliver consistent reports, but integration complexity is high due to franchise diversity.
- A fully federated system would preserve autonomy but fail on performance and consistent decision-making.
- A hybrid approach gives the best trade-off between central insight and practical franchise requirements.
- Phased implementation reduces risk and allows value delivery before full rollout.

### Justification

- Existing franchise varying PoS systems require flexible ingestion. A data lake supports this by storing raw data from all sources.
- Dimensional modeling simplifies reporting for business users and supports historical trend analysis.
- ELT uses modern warehouse processing power and retains source data for lineage and auditing.
- Role-based access and governance protect franchise data while enabling aggregated enterprise analysis.

## Logical Design

The logical design includes the following data entities and relationships:
- Dimensions: Outlet, Product, Time, Promotion, Franchisee.
- Facts: Sales, Margin, Inventory, FranchiseCosts.
- Relationships: FactSales links to Outlet, Product, Time, Promotion; FactMargin links to Outlet, Time, Product; FactInventory links to Outlet, Product, Time; FactFranchiseCosts links to Outlet, Franchisee, Time.

This structure supports common queries such as sales by product, outlet profitability, and campaign effectiveness.

## Physical Design

### Data Storage

- Raw data zone: object storage or staging database for PoS extracts, monthly reports, and finance files.
- Processed zone: cleansed tables or parquet files for standardized staging.
- Warehouse zone: optimized fact and dimension tables with partitioning by time and outlet.

### Performance Considerations

- Partition the fact tables by date and region to speed queries.
- Index or cluster on outlet and product keys for frequent joins.
- Use materialized views for common executive summaries.
- Apply compression and columnar storage where supported.

## Solution Architecture

The solution architecture comprises:
1. Source systems: legacy PoS, modern PoS, franchise reporting templates, finance/tax systems.
2. Ingestion layer: secure API, file upload portal, scheduled ETL jobs, and middleware connectors.
3. Data lake: raw data landing zone and curated staging zone.
4. Data warehouse: dimensional model and analytical repository.
5. Analytics layer: BI dashboards, reporting, and self-service exploration.
6. Governance/security: metadata catalog, data quality, access control, and lineage tracking.

## Conclusion

A phased hybrid data warehouse solution is the strongest fit for Eta-Beta-Pi. It allows OSIC to centralize analytics without forcing franchisees into a single back-office system. The approach balances immediate business value, practical data-loading concerns, and long-term enterprise governance.
