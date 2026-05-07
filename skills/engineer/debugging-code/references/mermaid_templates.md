# Debugging Diagram Templates (Mermaid)

Use these templates in `DEBUG_CONTEXT.md` to visualize system flow and failure location.

## 1. Data Pipeline Template
When to use: data ingestion, transformation, and persistence failures.
```mermaid
graph TD
  A[Raw Data] -->|Import| B[Transformer]
  B -->|Validated JSON| C{Business Logic}
  C -->|Result| D[Database]
  C --x|Bug: Null Check Missing| E[Internal Error 500]
```

## 2. API Request/Response Template
When to use: endpoint logic or contract mismatch issues.
```mermaid
graph LR
  U[User UI] -->|POST /login| A[Auth Controller]
  A -->|Verify Credentials| S[Auth Service]
  S -->|Query| DB[(User DB)]
  DB -->|Record Found| S
  S --x|Bug: Password Compare fails| A
  A -->|Error Response| U
```

## 3. UI Lifecycle Template
When to use: rendering, state update, and client-side crash issues.
```mermaid
graph TD
  A[Component Mount] --> B[useEffect: Fetch Data]
  B --> C[Set State: isLoading=false]
  C --> D[Render List]
  D --x|Bug: Data is undefined| E[White Screen/Crash]
```

## 4. State Machine Template
When to use: race conditions, retries, and async transition bugs.
```mermaid
stateDiagram-v2
  [*] --> IDLE
  IDLE --> PROCESSING: onClick
  PROCESSING --> SUCCESS: Complete
  PROCESSING --> FAILED: Error
  PROCESSING --> IDLE: Reset
  note right of PROCESSING : Bug: Race Condition here
```

## 5. Usage Rule
- Keep diagrams minimal and only include nodes relevant to current failure.
- Mark the suspected failure edge with `--x`.
- Update the diagram after root cause is confirmed.
