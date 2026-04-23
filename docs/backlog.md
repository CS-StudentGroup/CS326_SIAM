# Product Backlog — Pad Renting Management
---
## User Story 1 — Secure landlord login
| Field | Details |
| --- | --- |
| As a | landlord |
| I want | to securely log in |
| So that | unauthorized users cannot access my property data |
| Priority | High |
| Story points | 3 |
### Story 1 — Acceptance criteria
- User can log in with valid credentials.
- Error is shown for invalid login.
---
## User Story 2 — Add a new pad/room
| Field | Details |
| --- | --- |
| As a | landlord |
| I want | to add a new pad/room to the system |
| So that | I can track its availability |
| Priority | High |
| Story points | 5 |
### Story 2 — Acceptance criteria
- Can input room name and price.
- Cannot input negative price.
- New pad appears in the pad list.
---
## User Story 3 — Delete a pad
| Field | Details |
| --- | --- |
| As a | landlord |
| I want | to delete a pad from the system |
| So that | I can remove pads that are no longer available for rent |
| Priority | Medium |
| Story points | 2 |
### Story 3 — Acceptance criteria
- Can delete by ID.
- Item is removed from the list.
---
## User Story 4 — Register a new landlord (admin)
| Field | Details |
| --- | --- |
| As a | system admin |
| I want | to register a new landlord account |
| So that | they can use the platform |
| Priority | High |
| Story points | 3 |
### Story 4 — Acceptance criteria
- Registration validates email format.
- Password must be 8+ characters.
---
## User Story 5 — Secure logout
| Field | Details |
| --- | --- |
| As a | landlord |
| I want | to securely log out |
| So that | my session is terminated on shared devices |
| Priority | High |
| Story points | 1 |
### Story 5 — Acceptance criteria
- Session clears on logout.
- User is redirected to login.
---
## User Story 6 — Mark pad as occupied
| Field | Details |
| --- | --- |
| As a | landlord |
| I want | to mark a pad as occupied |
| So that | I know it is unavailable |
| Priority | Medium |
| Story points | 3 |
### Story 6 — Acceptance criteria
- Can toggle occupancy status (boolean).
---
## User Story 7 — Update monthly rental price
| Field | Details |
| --- | --- |
| As a | landlord |
| I want | to update the monthly rental price of a pad |
| So that | pricing stays current |
| Priority | Medium |
| Story points | 2 |
### Story 7 — Acceptance criteria
- Existing price can be overwritten.
- Validates for positive numbers.
---
## User Story 8 — Vacant pads dashboard
| Field | Details |
| --- | --- |
| As a | landlord |
| I want | to view a dashboard of all currently vacant pads |
| So that | I know what needs marketing |
| Priority | Low |
| Story points | 3 |
### Story 8 — Acceptance criteria
- List excludes occupied pads.
---
## User Story 9 — Assign tenant name to occupied pad
| Field | Details |
| --- | --- |
| As a | landlord |
| I want | to assign a specific tenant name to an occupied pad |
| So that | I can track who is in which unit |
| Priority | Low |
| Story points | 5 |
### Story 9 — Acceptance criteria
- Input field for tenant name is tied to pad ID.
---
## User Story 10 — Total potential revenue
| Field | Details |
| --- | --- |
| As a | landlord |
| I want | to calculate total potential revenue from all active pads |
| So that | I can see aggregate monthly income potential |
| Priority | Low |
| Story points | 2 |
### Story 10 — Acceptance criteria
- Sum equals the `monthly_price` of all pads in the system.
---
## User Story 11 — Generate monthly income report
| Field | Details |
| --- | --- |
| As a | landlord |
| I want | to generate a monthly income report |
| So that | I can review actual rental earnings from occupied pads for a given month |
| Priority | Low |
| Story points | 3 |
### Story 11 — Acceptance criteria
- Report shows each occupied pad with its tenant name and monthly price.
- Report displays total income from occupied pads only.
- Landlord can select the target month and year for the report.
---
## Summary
| # | Title | Priority | Points |
| --- | --- | --- | --- |
| 1 | Secure landlord login | High | 3 |
| 2 | Add pad/room | High | 5 |
| 3 | Delete pad | Medium | 2 |
| 4 | Register landlord (admin) | High | 3 |
| 5 | Secure logout | High | 1 |
| 6 | Mark pad occupied | Medium | 3 |
| 7 | Update rental price | Medium | 2 |
| 8 | Vacant pads dashboard | Low | 3 |
| 9 | Assign tenant name | Low | 5 |
| 10 | Total potential revenue | Low | 2 |
| 11 | Generate monthly income report | Low | 3 |
