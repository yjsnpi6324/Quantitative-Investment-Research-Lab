# Global Data Source Governance

## Purpose

Expand the A-share research system beyond China-only information sources while preserving source quality, independence, timestamp integrity, licensing/access constraints, and reproducibility.

The objective is not to collect the largest number of sources. It is to build a **diverse, tiered, cross-validated information network** that improves discovery, regime understanding, international spillover analysis, and resistance to single-source failure.

## Source domains

### 1. China / A-share primary sources

Use for domestic facts and first-party verification:

- CSRC, SSE, SZSE, BSE and exchange disclosures;
- listed-company announcements, filings and investor relations;
- PBOC, NBS, SAFE, NDRC, MOF and other relevant ministries;
- official industry associations and regulatory releases.

### 2. Global primary / official sources

Use for global macro, rates, liquidity, commodities, FX, policy and cross-market conditions:

- Federal Reserve, U.S. Treasury, SEC and CFTC;
- ECB, Bank of England, Bank of Japan and other major central banks;
- BIS, IMF, World Bank, OECD and major multilateral institutions;
- U.S. and international statistical agencies;
- official exchange, futures and commodity-market publications.

### 3. Global market / financial information

Use for market structure, price/volume context, earnings, corporate actions and cross-market comparison. Prefer providers with clear methodology, timestamps and historical coverage. Examples include Bloomberg, LSEG/Refinitiv, FactSet, S&P Global, ICE, CME and Nasdaq where access is available.

### 4. Global research / academic discovery

Use for new quantitative methods, market microstructure, forecasting, portfolio construction and empirical finance:

- arXiv;
- SSRN;
- NBER;
- RePEc/IDEAS;
- major peer-reviewed journals and conference proceedings;
- university research groups;
- reproducible open-source research repositories.

### 5. Global industry / technology sources

Especially important for the AI-sector task:

- company primary disclosures;
- semiconductor, cloud, data-center and equipment vendors;
- international industry bodies;
- reputable technical documentation and benchmark sources.

### 6. High-quality secondary sources

Use Reuters, AP, FT, WSJ, Nikkei Asia, The Economist and comparable reputable outlets for event discovery and synthesis. Secondary reporting must not replace primary-source verification when a primary source exists.

## Source selection rules

Every source is evaluated on:

- authority / first-party status;
- methodology transparency;
- timestamp precision;
- historical availability;
- update frequency;
- revision policy;
- geographic and market coverage;
- independence from other sources;
- accessibility / licensing constraints;
- known survivorship, selection or publication bias.

A large number of correlated sources does not equal source diversity. Ten outlets repeating the same wire story count as one information event for corroboration purposes.

## Source tiers

**Tier A — Primary / authoritative:** official filings, regulators, exchanges, central banks, statistical agencies and direct company disclosures.

**Tier B — High-quality institutional / academic:** established financial data providers, peer-reviewed research, major institutions and transparent research organizations.

**Tier C — High-quality secondary:** reputable financial/news/industry publications used primarily for discovery and cross-checking.

**Tier D — Discovery only:** social media, anonymous posts, unverified blogs, promotional research and opaque signal vendors. Never use Tier D alone as evidence for a production decision.

## Cross-market triangulation

For material predictions, seek independent evidence across at least two dimensions where applicable:

- domestic market data;
- global macro / rates / liquidity;
- overseas sector or asset-price signals;
- commodity / FX / rates spillovers;
- primary corporate / policy information;
- academic or empirical evidence.

Do not force cross-market evidence when it is economically irrelevant. Relevance beats source count.

## Time and look-ahead controls

- Record source timestamp and the information-availability timestamp whenever possible.
- Never use information that was not public at the forecast cutoff.
- Distinguish publication time from event time and revision time.
- Historical datasets must preserve vintage information where revisions could create look-ahead bias.
- Global market sources must respect the local trading-session boundary of the A-share forecast.

## Source lifecycle

`DISCOVERED → TRIAGED → VERIFIED → ACTIVE → DEGRADED → RETIRED`

A source can be active for discovery but unsuitable as a production evidence source. Reliability should be measured over time rather than assumed permanently.

## Task integration

Discovery Tasks should continuously search both domestic and international source domains. Material new sources enter the research system through a versioned source record and are evaluated before being promoted into routine production use.

Production Tasks should consume the current approved source registry rather than maintaining independent hard-coded source lists whenever practical.

## Research-method discovery

Global sources are also part of the New Quant Method Discovery pipeline. A new strategy, paper, benchmark, dataset or open-source implementation follows:

`Discovery → Intake → Triage → Reproduction → A-share Adaptation → OOS / Robustness → Challenger → Validated / Rejected`

No source or method becomes production simply because it is internationally prominent.

## Maintenance

Review source quality periodically. Prefer replacing weak sources over accumulating more low-quality sources. When a source is retired, preserve the reason and any historical dependency needed for reproducibility.
