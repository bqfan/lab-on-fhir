from ast import Tuple
from pydantic import BaseModel
from dataclasses import Field
from typing import Literal, Optional


"""
https://hl7.org/fhir/R4/observation-definitions.html#Observation.referenceRange
Observation.referenceRange
Element Id	Observation.referenceRange
Definition	
Guidance on how to interpret the value by comparison to a normal or recommended range.
Multiple reference ranges are interpreted as an "OR". In other words, to represent two distinct target populations,
two referenceRange elements would be used.
"""


"""
Observation.referenceRange.low
Element Id	Observation.referenceRange.low
Definition	
The value of the low bound of the reference range.
The low bound of the reference range endpoint is inclusive of the value (e.g. reference range is >=5 - <=9).
If the low bound is omitted, it is assumed to be meaningless (e.g. reference range is <=2.3).
"""

"""
Observation.referenceRange.high
Element Id	Observation.referenceRange.high
Definition	
The value of the high bound of the reference range.
The high bound of the reference range endpoint is inclusive of the value (e.g. reference range is >=5 - <=9).
If the high bound is omitted, it is assumed to be meaningless (e.g. reference range is >= 2.3).
"""


"""
Observation.referenceRange.type
Element Id	Observation.referenceRange.type
Definition	
Codes to indicate the what part of the targeted reference population it applies to.
For example, the normal or therapeutic range.
https://hl7.org/fhir/R4/valueset-referencerange-meaning.html
"""


"""
Observation.referenceRange.appliesTo
Element Id	Observation.referenceRange.appliesTo
Definition	
Codes to indicate the target population this reference range applies to.
For example, a reference range may be based on the normal population or a particular sex or race.
Multiple appliesTo are interpreted as an "AND" of the target populations.
For example, to represent a target population of African American females,
both a code of female and a code for African American would be used.
https://hl7.org/fhir/R4/valueset-referencerange-appliesto.html
"""


"""
Observation.referenceRange.age
Element Id	Observation.referenceRange.age
Definition	
The age at which this reference range is applicable.
This is a neonatal age (e.g. number of weeks at term) if the meaning says so.
"""

"""
Observation.referenceRange.text
Element Id	Observation.referenceRange.text
Definition	
Text based reference range in an observation which may be used
when a quantitative range is not appropriate for an observation.
An example would be a reference value of "Negative" or a list or table of "normals".
"""
class ReferenceRangeLow(BaseModel):
    value: float    # Numerical value (with implicit precision)
    comparator: Optional[Literal['<', '<=', '>=', '>']] = None # < | <= | >= | > - how to understand the value
    unit: Literal['mmHg']   # Unit representation
    system: Literal['http://unitsofmeasure.org']    # System that defines coded unit form
    code: Literal['mm[Hg]'] # Coded form of the unit


class ReferenceRangeHigh(BaseModel):
    value: float    # Numerical value (with implicit precision)
    comparator: Optional[Literal['<', '<=', '>=', '>']] = None # < | <= | >= | > - how to understand the value
    unit: Literal['mmHg']   # Unit representation
    system: Literal['http://unitsofmeasure.org']    # System that defines coded unit form
    code: Literal['mm[Hg]'] # Coded form of the unit


class ReferenceRange(BaseModel):
    high: Optional[ReferenceRangeHigh] = None
    low: Optional[ReferenceRangeLow] = None
    normalValue: Optional[list[str]] = None
    type: Optional[list[str]] = Literal[None, 'normal', 'recommended', 'treatment', 'therapeutic', 'pre', 'post']
    appliesTo: Optional[list[list[str]]] = None
    age: Optional[list[int]] = None
    text: Optional[list[str]] = None


class Coding(BaseModel):
    system: Literal["http://loinc.org", "http://snomed.info/sct"]
    code: str
    display: str


class Code(BaseModel):
    coding: list[Coding]
    text: str


class Reference(BaseModel):
    resourceType: Literal['Observation']
    status: str
    code: Code
    referenceRange: list[ReferenceRange]

{
  "resourceType": "Observation",
  "status": "unknown",
  "code": {
    "coding": [
      {
        "code": "15074-8",
        "display": "Glucose [Moles/volume] in Blood",
        "system": "http://loinc.org1"
      }
    ],
    "text": "Glucose"
  },
  "referenceRange": [
    {
      "low": {
        "code": "mmol/L",
        "system": "http://unitsofmeasure.org",
        "unit": "mmol/l",
        "value": 3.1
      },
      "high": {
        "code": "mmol/L",
        "system": "http://unitsofmeasure.org1",
        "unit": "mmol/l",
        "value": 6.2
      }
    }
  ]
}