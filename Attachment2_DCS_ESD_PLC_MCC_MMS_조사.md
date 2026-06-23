# [Attachment 2] DCS · ESD · PLC 상세 조사 및 MCC · MMS와의 관계

> FAT Lesson & Learned Group Study 성과품 (Appendix)
> 작성: 조혜준 대리 | 작성일: 2026-06-23
> 목적: 제어/안전 시스템(DCS, ESD, PLC)의 정의·차이를 명확히 하고, 전기설비(MCC)·회전기계 보호(MMS)와의 인터페이스 관계를 정리하여, FAT 단계에서 시스템 경계(Boundary)·신호 인터페이스 오류로 인한 MH 낭비를 방지한다.

---

## 0. 요약 (한 장 정리)

| 구분 | 역할 | 핵심 키워드 | 표준 |
|---|---|---|---|
| **DCS** | 공정 **제어·운전 최적화** (정상 운전) | 연속/아날로그 제어, 중앙 집중 | IEC 61131 등 (BPCS) |
| **ESD** | **비상 정지** (안전한 상태로) | Shutdown, Logic Solver | IEC 61508 / 61511 (SIS) |
| **PLC** | 개별 기계/공정의 **이산 제어** | 빠른 Logic, 디지털 | IEC 61131 |
| **MCC** | 전동기 **전원 공급·기동/정지** (전기) | Feeder, VFD, Starter | IEC 61439 등 |
| **MMS** | 회전기계 **진동·축위치 보호** | Vibration, Trip | **API 670** |

> **한 줄 요약**: DCS·PLC는 "잘 돌리는 것(Control)", ESD는 "위험할 때 안전하게 멈추는 것(Safety)", MCC는 "전동기에 전기를 주고 받는 것(Power)", MMS는 "회전기계가 망가지기 전에 잡는 것(Protection)". 이들이 **신호로 연결(Interface)** 되어 하나의 플랜트 자동화 시스템을 구성한다.

---

## 1. DCS (Distributed Control System, 분산제어시스템)

### 정의
- 플랜트 전반의 **연속 공정(continuous process)을 중앙에서 집중 제어·감시**하는 시스템.
- "Distributed(분산)" = 제어 기능을 현장 분산 컨트롤러에 나누어 배치하되, 운전은 중앙 제어실(Operator Station)에서 통합 감시.
- 안전 용어로는 **BPCS (Basic Process Control System)** 라고도 부른다.

### 특징
- 다수의 공정 루프(온도·압력·유량·레벨 등)를 **PID 등 아날로그/연속 제어**로 운전.
- HMI(Operator Graphic), Historian, Alarm 관리, Faceplate 기반 운전이 강점.
- 대표 Vendor: Honeywell(Experion), Yokogawa(Centum), Emerson(DeltaV), ABB(800xA), Siemens 등.

### FAT L&L 시사점
- BCC FAT 사례처럼 **Faceplate로 Valve Open/Close, Pump Start/Stop을 구현 가능** → 별도 Hand Switch나 과도한 Logic 작성이 불필요한 경우가 많다.
- DCS는 "정상 운전 최적화"가 목적이며, **안전 정지는 DCS가 아니라 ESD가 담당**(독립성 원칙).

---

## 2. ESD (Emergency Shutdown System, 비상정지시스템)

### 정의
- 비상 상황(이상 고압, 화재, 가스 누출 등) 발생 시 **설비를 안전한 상태(Safe State)로 정지**시켜 인명·환경·자산을 보호하는 시스템.
- ESD는 더 넓은 개념인 **SIS(Safety Instrumented System)의 일부 = "Logic Solver"** 에 해당한다.

### SIS와 ESD의 관계
- **SIS = 안전계장시스템** 으로 3가지로 구성:
  1. **현장 계기(Sensor)** — 안전용 트랜스미터/스위치
  2. **Logic Solver** — 안전용 로직 처리부 ← **여기가 ESD(또는 ESD 시스템)**
  3. **Actuator(최종요소)** — 안전용 밸브(ESDV/SDV) 등
- 즉, **ESD ⊂ SIS**. 전통적 ESD 시스템은 SIS의 Logic Solver 부분만을 지칭하며, 역시 안전 목적으로 설계된다.

### 특징
- **DCS보다 훨씬 엄격한 신뢰성·가용성 요구** (SIL 등급, IEC 61508/61511).
- 표준상 **SIS(ESD)와 DCS의 하드웨어는 독립(Independent)** 되어야 한다 → 별도 Logic Solver, 별도 I/O.
- "Fail-safe(고장 시 안전측)" 설계가 기본.

### FAT L&L 시사점
- BCC APCS FAT 사례의 **Pre-alarm ESD 누락**, **ESD On-off valve switch** 등은 모두 ESD 영역.
- ESD는 안전 기능이므로 **DCS Faceplate 편의기능과 혼동하지 말 것** — 안전 관련 로직은 누락/오설계 시 치명적.

---

## 3. PLC (Programmable Logic Controller, 프로그래머블 로직 컨트롤러)

### 정의
- **개별 기계 또는 단위 공정(skid, package)을 제어**하는 프로그래머블 컨트롤러.
- 본래 릴레이 로직 대체용으로 출발 → 빠른 **이산(Discrete)·디지털 로직** 처리에 강점.

### 특징
- 처리 속도가 빠르고 구조가 단순/경제적 → 패키지 장비(컴프레서, 보일러, 워터트리트먼트 등) 로컬 제어에 다수 사용.
- 안전용으로 인증된 **Safety PLC**는 ESD/SIS의 Logic Solver로도 사용된다.
- 대형 플랜트에서는 다수의 PLC가 **상위 DCS와 통신(Modbus, OPC 등)** 하여 통합 감시됨.

### DCS vs PLC 관점
- 과거: PLC=이산제어/소규모, DCS=연속제어/대규모로 명확히 구분.
- 현재: 경계가 흐려짐(PLC도 PID·HMI 지원, DCS도 빠른 로직 지원). 그러나 **PLC=단위 기계/패키지, DCS=플랜트 전체 통합**이라는 역할 구분은 유효.

---

## 4. DCS · ESD · PLC 차이점 (핵심 비교)

| 항목 | DCS | ESD (SIS) | PLC |
|---|---|---|---|
| **목적** | 공정 제어·운전 최적화 | 비상 정지 / 안전 확보 | 개별 기계·단위공정 제어 |
| **운전 상태** | 정상 운전(Normal) | 비상 상황(Abnormal) | 정상 운전(단위) |
| **제어 성격** | 연속/아날로그(PID) | 이산/안전 로직 | 이산/디지털(고속) |
| **신뢰성 요구** | 표준 수준 | **매우 높음 (SIL, IEC 61508/61511)** | 용도별(Safety PLC 별도) |
| **독립성** | — | DCS와 **HW 독립 필수** | 상위 DCS에 통합 가능 |
| **고장 철학** | 가용성 우선 | **Fail-safe(안전측)** | 용도별 |
| **적용 범위** | 플랜트 전체 | 안전 기능(Trip) | 패키지/Skid 단위 |
| **대표 예** | 온도·유량 루프 제어 | 고압 시 설비 Trip | 컴프레서 패키지 제어 |

### 관계 정리
```
        [SIS = 안전계장시스템]
   Sensor → [Logic Solver = ESD] → Actuator(ESDV)
                  │ (독립, IEC 61508/61511)
   ───────────────┼───────────────────────────
   [BPCS = DCS]  공정 정상 운전 제어 (PID, HMI)
        │
   [PLC] 패키지/단위 기계 제어 → 상위 DCS로 통신
```
- **DCS(BPCS)와 ESD(SIS)는 독립**되어야 하지만, 운전 편의를 위해 **통합 HMI**로 감시하는 경우가 많다(Integrated vs Separated 논쟁 존재).
- PLC는 단위 제어를 맡고 상위 DCS로 데이터를 올린다.

---

## 5. MCC (Motor Control Center, 전동기 제어반)

### 정의
- 플랜트 내 **전동기(Motor)에 전원을 공급하고 기동/정지·보호**하는 **전기 설비**.
- 다수의 Feeder(기동기/Starter, VFD/인버터, 차단기)를 하나의 패널 집합으로 모아 놓은 것.

### DCS / PLC 와의 관계 (인터페이스 철학)
- **Pump/Motor의 Start/Stop은 본질적으로 MCC가 수행**한다. DCS/PLC는 MCC로 **명령(Start/Stop)을 보내고 상태(Run/Trip)를 받는다.**
- 전통적 방식: DCS/PLC와 MCC 사이에 **IRP(Interposing Relay Panel)** 를 설치 → 서로 다른 전압 신호 절연 및 DCS/PLC 카드 보호.
- 신호 종류:
  - DCS/PLC → MCC: Start/Stop 명령(DO), VFD 속도 Setpoint(AO, 4~20mA)
  - MCC → DCS/PLC: Run/Stop/Trip 상태(DI), 전류(A)·속도(RPM) 지시(AI, 4~20mA)
- **Smart/Intelligent MCC**: Ethernet/**Modbus TCP/IP**/Profibus 통신으로 DCS와 직접 연동 → 전력·에너지·정비 데이터를 DCS에서 직접 조회(예지정비 활용).

### FAT L&L 시사점 (중요)
- MOM에 명시된 대로, **Pump Start/Stop을 DCS Interlock으로 과도하게 구현하지 말고 MCC로 연결**하면 되는 경우가 많다.
- 즉, "전동기 기동/정지" 같은 기능은 **MCC의 역할**임을 인지하면 불필요한 DCS Logic·Hand Switch 작성을 피할 수 있다 → MH 절감.

---

## 6. MMS (Machinery Monitoring System, 회전기계 감시/보호 시스템)

### 정의
- 터빈·컴프레서·대형 펌프 등 **회전기계(Rotating Machinery)의 진동(Vibration)·축위치(Axial/Thrust)·속도** 등을 연속 감시하고, 위험 시 **Trip(보호)** 시키는 시스템.
- 대표 제품: **Bently Nevada 3500 / Orbit 60** (Baker Hughes).

### 표준
- **API 670 (Machinery Protection System)** 준수가 핵심 (석유·가스 회전기계 보호 표준).
- 왕복동 압축기: API 618도 관련.

### DCS / ESD 와의 관계
- MMS는 **독립적 보호 시스템**이지만, 측정·트립 신호를 상위 시스템과 주고받는다:
  - **DCS/SCADA 연동**: Ethernet, **Modbus TCP/RTU, OPC-UA**로 진동·축위치 데이터를 DCS로 전송 → 운전원이 중앙에서 감시.
  - **ESD/Trip 연동**: 릴레이 모듈(예: 3500/32)의 **건접점(dry contact) 출력**으로 **Trip 로직(ESD)·알람 annunciator**에 연결 → 회전기계 자동 보호.
- 즉, **MMS는 "회전기계 전용 보호 계층"** 으로서 ESD(안전정지)와 협력하고, 감시 데이터는 DCS로 올린다.

### FAT L&L 시사점
- BCC APCS FAT 사례의 **"Gas Detector for Rotating"** 등 회전기계 관련 이슈는 MMS/보호 인터페이스 영역과 맞닿음.
- MMS ↔ ESD ↔ DCS 신호 경계(누가 Trip을 결정하고, 누가 표시만 하는지)를 명확히 해야 FAT 시 혼선·재작업 방지.

---

## 7. 전체 관계 종합도

```
        ┌─────────────────────── 중앙 제어실(Operator) ───────────────────────┐
        │                                                                     │
   ┌────┴────┐        ┌──────────┐         ┌──────────┐        ┌──────────┐
   │   DCS   │◄──────►│   ESD    │         │   PLC    │◄──────►│   MMS    │
   │ (BPCS)  │ 독립   │  (SIS)   │         │(Package) │ 신호   │(API 670) │
   │ 공정제어 │        │ 비상정지  │         │ 단위제어  │        │ 회전기계  │
   └────┬────┘        └────┬─────┘         └────┬─────┘        └────┬─────┘
        │ 명령/상태          │ Trip                │                   │ Trip/Data
        │ (IRP 경유)         ▼                    │                   ▼
        └──────────────►┌──────────┐◄────────────┘            회전기계(Turbine,
            Start/Stop  │   MCC    │  전원공급·기동/정지         Compressor)
            Speed SP    │ (Motor)  │  (Modbus TCP)
                        └────┬─────┘
                             ▼
                          전동기(Motor / Pump)
```

### 핵심 정리 (3줄)
1. **DCS = 운전(Control)**, **ESD = 안전정지(Safety, SIS의 Logic Solver)**, **PLC = 단위기계 제어** — 셋은 목적·신뢰성·독립성이 다르다.
2. **MCC**는 전동기에 전원을 주고 기동/정지하는 전기설비로, DCS/PLC와 **명령·상태 신호(IRP 또는 Modbus)** 로 연결된다 → 펌프 기동/정지는 MCC 영역.
3. **MMS**는 회전기계 진동/축위치를 감시·보호(API 670)하며, **Trip은 ESD**로, **데이터는 DCS**로 전달한다.

---

## 부록: 출처 (Sources)

- [Differences Between SIS, ESD, DCS, and PLC – Just Measure it](https://zeroinstrument.com/differences-between-sis-esd-dcs-and-plc-in-industrial-control-systems/)
- [The difference between SIS and ESD, DCS, PLC – Qiming Automation](https://www.abbgedcs.com/the-difference-between-sis-and-esd-dcs-plc/)
- [PLC vs DCS vs SIS Control Systems – Tango Valve](https://www.tangovalve.com/plc-vs-dcs-vs-sis-control-systems/)
- [Integrated SIS DCS or separate? – Abhisam](https://www.abhisam.com/integrated-safety-instrumented-system-sis-distributed-control-system-dcs/)
- [Distributed Control System & Motor Control Center Interface Philosophy – Instrumentation Tools](https://instrumentationtools.com/distributed-control-system-motor-control-center-interface-philosophy/)
- [Integrating Low Voltage Motor Control Centers into DCS – Rockwell Automation](https://literature.rockwellautomation.com/idc/groups/literature/documents/at/mcc-at008_-en-p.pdf)
- [Intelligent Motor Control Center Fundamentals – Eaton](https://www.eaton.com/us/en-us/catalog/low-voltage-power-distribution-controls-systems/low-voltage-motor-control-centers/intelligent-motor-control-center-fundamentals.html)
- [Bently Nevada 3500 Machinery Protection Systems – Baker Hughes](https://www.bakerhughes.com/bently-nevada/monitoring-systems/machinery-protection/3500-machinery-protection-systems)
- [Orbit 60 Series Update: API 670 – Baker Hughes](https://www.bakerhughes.com/bently-nevada/orbit-home/orbit-article/orbit-60-series-update-api-670)
