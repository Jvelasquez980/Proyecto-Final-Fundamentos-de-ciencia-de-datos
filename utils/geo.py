from __future__ import annotations

import csv
import io


_STATE_CSV = """State,Code
Alabama,AL
Alaska,AK
Arizona,AZ
Arkansas,AR
California,CA
Colorado,CO
Connecticut,CT
Delaware,DE
District of Columbia,DC
Florida,FL
Georgia,GA
Hawaii,HI
Idaho,ID
Illinois,IL
Indiana,IN
Iowa,IA
Kansas,KS
Kentucky,KY
Louisiana,LA
Maine,ME
Maryland,MD
Massachusetts,MA
Michigan,MI
Minnesota,MN
Mississippi,MS
Missouri,MO
Montana,MT
Nebraska,NE
Nevada,NV
New Hampshire,NH
New Jersey,NJ
New Mexico,NM
New York,NY
North Carolina,NC
North Dakota,ND
Ohio,OH
Oklahoma,OK
Oregon,OR
Pennsylvania,PA
Rhode Island,RI
South Carolina,SC
South Dakota,SD
Tennessee,TN
Texas,TX
Utah,UT
Vermont,VT
Virginia,VA
Washington,WA
West Virginia,WV
Wisconsin,WI
Wyoming,WY
"""


def _build_state_to_code() -> dict[str, str]:
    reader = csv.DictReader(io.StringIO(_STATE_CSV.strip()))
    return {row["State"]: row["Code"] for row in reader}


STATE_TO_CODE = _build_state_to_code()
