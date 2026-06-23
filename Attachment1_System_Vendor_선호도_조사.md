# [Attachment 1] 국가별 · 사업주별 System Vendor 선호도 조사

> FAT Lesson & Learned Group Study 성과품 (Appendix)
> 작성: 조혜준 대리 | 작성일: 2026-06-23
> 목적: System Vendor별 선호도를 국가/사업주 단위로 정량 파악하여, 향후 PJT 입찰·설계 단계에서 Vendor 특성을 사전 반영 → MH 절감 및 설계 품질 향상

---

## 0. 요약 (Executive Summary)

- 글로벌 DCS 시장은 **ABB, Emerson, Honeywell, Siemens, Yokogawa 5개 사가 전체 매출의 약 60~65%를 점유**하는 과점 구조이다.
- 그러나 **지역(국가)별 / 사업주별로 선호 Vendor가 뚜렷하게 갈린다.** 즉 "글로벌 점유율"과 "특정 PJT에서 실제 채택되는 Vendor"는 다르며, 이는 사업주의 **AVL(Approved Vendor List)** 과 표준에 의해 결정된다.
- 핵심 패턴:
  - **북미** → Emerson(DeltaV), Honeywell 강세
  - **일본/동아시아** → Yokogawa 절대 강세 (APAC 지역 점유율 37.6%)
  - **중국** → 로컬 Vendor(Supcon 40.4%, Hollysys 17.2%)가 시장의 약 58% 장악
  - **중동(GCC)** → 사업주 AVL 기반, Honeywell/Yokogawa/Emerson 3강
  - **러시아/CIS** → GOST 인증 + 서방 Vendor 철수로 로컬·중국 Vendor 비중 증가
- 본 조사 결과는 입찰 단계에서 "이 사업주/국가에서는 이 Vendor가 유력하다"는 **사전 가늠자**로 활용한다.

---

## 1. 글로벌 DCS 시장 개요 (정량)

| 구분 | 수치 | 비고 |
|---|---|---|
| 2024년 글로벌 DCS 시장 규모 | 약 USD 174.3억 | 2034년 USD 275.3억 전망 (CAGR 6.7%) |
| Top 5 Vendor 합산 점유율 | 약 60~65% | ABB, Emerson, Honeywell, Siemens, Yokogawa |
| 최대 수요 지역 | Asia-Pacific (34~39%) | 산업화·에너지 투자 견인 |
| 단일 국가 최대 시장 | 미국 (약 21.3%) | R&D·인프라 |

### 지역별 시장 점유율 (2024, 출처 간 편차 있음)

| 지역 | 점유율(대표값) | 특징 |
|---|---|---|
| Asia-Pacific | 약 34~39% | 최대 시장, 6,000+ installations, 중·일·인도·한국 주도 |
| North America | 약 29~35% | 성숙 시장, 최대 단일국 = 미국 |
| Europe | 약 27% | 성숙 시장 |
| Middle East & Africa | 약 5% | 신흥, 가장 빠른 성장(CAGR ~6.2%) |

> ※ 시장조사기관(Mordor, Credence, MarketReportsWorld 등)별 정의·집계 방식 차이로 ±5%p 편차 존재. 절대값보다 **상대적 우열 패턴**에 주목할 것.

---

## 2. 국가/지역별 Vendor 선호도

### 2-1. 북미 (North America)
- **선호 Vendor: Emerson(DeltaV) 1순위, Honeywell 2순위**
- Emerson은 현지 지원·서비스 망이 강해 "Local support 우선" PJT에서 우위.
- Oil & Gas, 정유, 화학 분야 레퍼런스가 두텁다.

### 2-2. 일본 및 동아시아 (Japan / East Asia)
- **선호 Vendor: Yokogawa 절대 강세**
- Yokogawa는 **APAC 지역 점유율 약 37.6%**, 업계 최고 수준의 **MTBF(Mean Time Between Failures)** 를 보유.
- 고위험 화학 공정(High-risk chemical processing)에서 신뢰성 기반으로 선호도 1위.
- 일본 사업주(JGC, Chiyoda, Toyo 등 EPC 및 일본계 Owner) PJT에서는 Yokogawa가 사실상 기본값.

### 2-3. 중국 (China) — 로컬 Vendor 우위
2024년 중국 DCS 시장 점유율:

| Vendor | 점유율 | 구분 |
|---|---|---|
| **Supcon (中控)** | **40.4%** | 로컬 (1위) |
| **Hollysys (和利时)** | **17.2%** | 로컬 (2위) |
| Emerson | 9.8% | 글로벌 |
| Yokogawa | 5.6% | 글로벌 |
| Siemens | 5.5% | 글로벌 |
| ABB | 4.5% | 글로벌 |
| Honeywell | 4.2% | 글로벌 |
| Others | 17.1% | - |

- **로컬 2사(Supcon+Hollysys) 합산 약 57.6%** → 중국 내수 PJT는 로컬 Vendor가 디폴트.
- 중국계 EPC/Owner 발주 PJT 입찰 시 Supcon/Hollysys 대응 역량을 사전 검토 필요.

### 2-4. 중동 GCC (Saudi/UAE/Kuwait/Bahrain 등)
- 선호 Vendor: **Honeywell, Yokogawa, Emerson 3강** (사업주 AVL이 최종 결정).
- 중동/동남아에서는 **Emerson의 Dubai 재고(현지 stock) 보유**가 강점으로 작용.
- Vendor 선정의 핵심은 **사업주 AVL 등재 여부** → 아래 §3 참조.

### 2-5. 러시아 / CIS
- 2023년 러시아 DCS 시장 약 USD 7.29억, 저성장(CAGR ~0.9%).
- **2022년 이후 ABB 등 서방 Vendor 철수**, 국제 제재로 글로벌 Vendor 공급 제약.
- 결과적으로 **로컬 Vendor 및 중국 Vendor 비중 확대**, **GOST 표준 준수**가 필수 (BCC PJT의 GOST steam flow compensation 이슈와 동일 맥락).

### 2-6. 한국 / 유럽
- 한국: 글로벌 5사 + 국내 PLC/제어 솔루션 혼재. 발주처(정유·석화 대기업) 표준에 따라 결정.
- 유럽: **Siemens(독일계), ABB** 강세, 성숙 시장.

### 국가별 선호도 요약표

| 국가/지역 | 1순위 | 2순위 | 결정 요인 |
|---|---|---|---|
| 북미 | Emerson | Honeywell | 현지 지원망 |
| 일본/동아시아 | Yokogawa | - | MTBF·신뢰성 |
| 중국 | Supcon(40.4%) | Hollysys(17.2%) | 로컬·가격 |
| 중동 GCC | Honeywell/Yokogawa | Emerson | 사업주 AVL |
| 러시아/CIS | 로컬·중국 | - | GOST·제재 |
| 유럽 | Siemens | ABB | 현지·표준 |

---

## 3. 사업주(Owner)별 선호도 — AVL 중심

> 핵심: Oil & Gas 메이저 사업주는 **AVL(Approved Vendor List)** 로 사용 가능 Vendor를 통제한다. Vendor가 AVL에 없으면 기술적으로 우수해도 채택 불가. 따라서 사업주별 선호는 곧 **"AVL + 사업주 표준(Owner Spec)"** 을 의미한다.

| 사업주 | 국가 | 비고 / 선정 체계 |
|---|---|---|
| **Saudi Aramco** | 사우디 | Vendor Code(고유 디지털 코드) 부여 + 사전자격(prequalification)·기술평가·현장감사·재무/규제 적합성 심사. SAES/SAEP 사내표준 준수 필수 |
| **ADNOC** | UAE | 4,200+ 사전검증 Vendor 보유. ISO 9001/14001, API Q1/Q2 등 국제표준 + ADNOC Code of Conduct 준수 |
| **기타 GCC** (Bapco, KNPC, DEWA, SWCC, NWC, KOC 등) | GCC | 각사 Vendor Approval 프로세스 보유, 별도 AVL 운영 |

### 시사점 (FAT L&L 관점)
- 사업주 AVL/Spec을 **입찰 단계에서 확보**하면, 어떤 Vendor가 들어올지 사전 예측 가능 → BCC FAT에서 발생한 "Vendor Logic 설계 특성 미인지로 인한 MH 낭비"를 방지.
- 예: AIS(Vendor)는 Faceplate로 Valve open/close 구현이 가능했음에도 P&ID/Logic description에 불필요하게 반영 → 사업주/Vendor 표준을 사전에 알았다면 회피 가능.
- **→ 결론: "국가 + 사업주 AVL + Vendor 표준" 3중 조합으로 사전 가늠 → Checklist화.**

---

## 4. 회사 수주 PJT 사업주별 Vendor 선호 경향

> **작성 기준(반드시 확인):** 아래는 ① 사업주 모회사의 Preferred Supplier/사내표준, ② 공개 레퍼런스, ③ 지역·산업별 설치기반 경향을 종합한 **추정치**다. 동일 사업주라도 PJT·시점·EPC에 따라 달라지므로 실제 적용 시 해당 PJT의 **AVL/I&C Spec을 반드시 재확인**할 것.

### 4-1. 사우디 (Saudi Arabia)
요약 — **Aramco 계열**: Honeywell(Experion) 최대 설치기반, 정유부문은 Yokogawa(CENTUM)도 강세 / **SABIC 계열**: Yokogawa를 Preferred Supplier로 지정(+Jubail 단지 Honeywell 다수). ESD=Triconex, MMS=Bently Nevada가 사실상 표준.

| 사업주 | 모회사 / 성격 | 유력 Vendor 경향 |
|---|---|---|
| Al‑Jubail Petrochemical (KEMYA) | SABIC + ExxonMobil JV | Yokogawa / Honeywell |
| Saudi Kayan Petrochemical | SABIC | Yokogawa / Honeywell |
| SAMAPCO (Sahara & Ma'aden) | Sahara + Ma'aden JV | Yokogawa / Honeywell |
| TASNEE | Saudi 민영 석화 | Honeywell / Yokogawa |
| PetroRabigh | Aramco + Sumitomo JV | Honeywell / Yokogawa |
| SADARA Chemical Co. | Aramco + Dow JV | Honeywell / Yokogawa (Dow는 Emerson 선호 경향) |
| YASREF | Aramco + Sinopec JV | Honeywell / Yokogawa |
| SATORP | Aramco + TotalEnergies JV | Honeywell / Yokogawa |
| Saudi Arabian Mining Co. (Ma'aden) | 광물·인산(국영) | Honeywell / Yokogawa |

※ 최종 결정 변수: Aramco Vendor Code/AVL 및 SAES·SAEP, SABIC Engineering Standard.

### 4-2. 쿠웨이트 · 오만
| 사업주 | 국가 | 유력 Vendor 경향 |
|---|---|---|
| Kuwait National Petroleum Co. (KNPC) | 쿠웨이트 | Honeywell 강세 / Yokogawa · Emerson |
| Kuwait Oil Company (KOC) | 쿠웨이트 | Honeywell 강세 / Yokogawa · Emerson |
| ORPIC (現 OQ) | 오만 | Honeywell / Yokogawa |

### 4-3. 한국
요약 — 한국 정유·석화는 Yokogawa·Honeywell 양강, Emerson도 사용. 발주처 표준에 따라 결정.

| 사업주 | 성격 / 비고 | 유력 Vendor 경향 |
|---|---|---|
| S‑Oil Corporation | 정유·석화 (Saudi Aramco 자회사) | Yokogawa / Honeywell · Emerson |
| LG화학 | 종합 석화 | Yokogawa / Honeywell |
| Lotte Chemical | 종합 석화 | Yokogawa / Honeywell |
| Yeochun NCC (YNCC) | NCC (한화·DL·롯데 JV) | Yokogawa / Honeywell |
| DL Chemical | 석화 (DL그룹) | Yokogawa / Honeywell |
| Tongsuh Petrochemical | Asahi Kasei 자회사 | Yokogawa (일본계 모회사 선호) |
| INNOX LITHIUM | 2차전지 소재 | PLC 기반 + DCS(Yokogawa/Honeywell) 혼용 |
| TLC | 석화 관련 | Yokogawa / Honeywell |

### 4-4. 러시아 · CIS
요약 — Sibur·Gazprom 계열 가스/석화 PJT는 Yokogawa 레퍼런스가 두텁고 Honeywell도 사용. 단 2022년 이후 서방 Vendor 철수·제재로 **로컬·중국 Vendor 대체 가능성 및 GOST 표준 준수**가 핵심 변수.

| 사업주 | 모회사 / 성격 | 유력 Vendor 경향 · 비고 |
|---|---|---|
| NKNH (Nizhnekamskneftekhim) | Sibur 자회사 | Yokogawa / Honeywell · GOST 필수 |
| LLC "Amur GCC" (AGCC) | Sibur (대형 GCC) | Yokogawa 등 · 제재 영향 주의 |
| JSC Gazpromneft MNPZ | Gazprom Neft (모스크바 정유) | Honeywell / Yokogawa · GOST |
| Gazpromneft | Gazprom Neft (국영계) | Honeywell / Yokogawa · GOST |
| BCC (Baltic Chemical Complex) | RusGazDobycha/Gazprom 계열 | 본 L&L 대상 PJT · GOST(Steam compensation) 이슈 |

### 4-5. 동남아 (말레이시아 · 필리핀)
| 사업주 | 국가 / 모회사 | 유력 Vendor 경향 |
|---|---|---|
| Pengerang Intermediate Chemicals | 말레이 (Asahi Kasei+Petronas+Mitsubishi) | Yokogawa (일본계 JV) / Honeywell |
| LG PETRONAS Chemicals Malaysia | 말레이 (LG Chem+Petronas JV) | Honeywell / Yokogawa |
| Petron Malaysia Refining & Marketing | 말레이 (Petron) | Yokogawa / Honeywell |
| Petron Corporation | 필리핀 | Yokogawa / Honeywell |
| JG Summit Petrochemical Corp. | 필리핀 | Yokogawa / Honeywell |

※ Petronas 계열은 PTS(Petronas Technical Standard)·AVL 운영. 일본계 JV는 Yokogawa 선호 경향.

### 4-6. 미국 · 중국
| 사업주 | 국가 / 성격 | 유력 Vendor 경향 |
|---|---|---|
| CPChem (Chevron Phillips Chemical) | 미국 석화 | Emerson(DeltaV) / Honeywell (북미 강세) |
| DL Chemical / REXtac LLC JV | 미국(Texas) 석화 JV | Emerson / Honeywell |
| Cariflex | 합성고무 (DL Chemical 소유) | Yokogawa / Honeywell (Plant 소재지 표준 영향) |
| BASF Polyurethanes Chongqing | 중국 (BASF 자회사) | BASF 그룹표준 Siemens(PCS 7) / Emerson 경향 |

※ 중국 내 다국적 JV(BASF 등)는 로컬 Vendor보다 모회사 글로벌 표준(Siemens/Emerson)을 따르는 경우가 많아, 중국 내수 로컬 우위(Supcon·Hollysys)와 구분할 것.

### 종합 시사점
- 중동(사우디·쿠웨이트·오만) PJT → **Honeywell·Yokogawa 2강 + 사업주 AVL** 핵심, ESD=Triconex/MMS=Bently Nevada 사실상 고정.
- 한국·동남아·러시아 PJT → **Yokogawa 비중 높음**(일본계 모회사·가스석화 레퍼런스).
- 북미(CPChem 등)→ Emerson, 중국 다국적 JV → Siemens/Emerson 등 모회사 표준 경향.
- → 입찰 단계 1차 필터로 사용하되 **"모회사 표준 + PJT AVL" 2단 확인** 후 Vendor Logic 특성을 사전 반영.

---

## 5. 활용 방안 (성과품 연계)

1. 입찰/Kick-off 단계에서 본 표를 활용해 **유력 Vendor 후보군**을 미리 좁힌다.
2. 해당 Vendor의 Logic 설계 특성(Faceplate 기반 Valve 제어, Pump Start/Stop의 MCC 연계 등)을 사전 적용 → 불필요한 P&ID/Logic 작업 제거.
3. 국가/사업주/Vendor별 **주의사항 Checklist**(성과품 핵심)에 본 선호도 데이터를 1차 필터로 삽입.

---

## 부록: 출처 (Sources)

- [Yokogawa & SABIC Preferred Supplier / Co-innovation – Control.com](https://control.com/news/yokogawa-and-sabic-team-up-petrochemical-process-optimization/)
- [Honeywell Process Solutions (Aramco·SABIC 설치기반) – Razz Middle East](https://razz.sa/en/instrumentation/honeywell-process)
- [Distributed Control System Market – Intel Market Research](https://www.intelmarketresearch.com/distributed-contorl-system-market-24242)
- [Distributed Control System Market – Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/distributed-control-system-market)
- [China Chinese DCS Vendors Gain Local Market Share – Automation World](https://www.automationworld.com/products/control/news/13302870/china-chinese-dcs-vendors-gain-local-market-share)
- [Russia Distributed Control System Market – NextMSC](https://www.nextmsc.com/report/russia-distributed-control-system-market)
- [DCS Market in APAC Region – PRNewswire](https://www.prnewswire.com/news-releases/dcs-market-in-the-apac-region-2014-2018-key-vendors-are-abb-emerson-honeywell-siemens-and-yokogawa-electric-281590231.html)
- [Saudi Aramco Vendor Code & Approved List 2021-2026 – Farmonaut](https://farmonaut.com/mining/saudi-aramco-vendor-code-approved-list-2021-2026)
- [ADNOC Approved Vendor List (AVL) Guide – Alliance Fittings](https://alliancefittings.net/blog/f/adnoc-approved-vendor-list-avl-complete-guide-for-uae-oil-gas)
- [DCS Regional Market Share – Credence Research](https://www.credenceresearch.com/report/distributed-control-systems-dcs-market)
- [Top DCS Systems in the World – WOIN/Medium](https://medium.com/@woin/top-dcs-systems-in-the-world-ea74ae4a95cb)

> ※ 본 문서의 수치는 공개된 시장조사기관 자료 기반이며 기관별 편차가 존재함. 실제 PJT 적용 시 해당 사업주의 최신 AVL/Spec을 별도 확인할 것.
