import pytest
from pydantic import ValidationError
from fhirlab.web.api.references.schema import ReferenceRangeHigh, ReferenceRangeLow, ReferenceRange


@pytest.mark.anyio
async def test_reference_range_low() -> None:
    """
    # Checks pandantic model ReferenceRangeLow.

    # :param value: ReferenceRangeLow value.
    # :param comparator: ReferenceRangeLow comparator.
    # :param unit: ReferenceRangeLow unit.
    # :param system: ReferenceRangeLow system.
    # :param code: ReferenceRangeLow code.
    """
    low = ReferenceRangeLow(value=2.1, comparator='>', unit='mmHg', system='http://unitsofmeasure.org', code='mm[Hg]')

    assert low.value == 2.1
    assert low.comparator == '>'
    assert low.unit == 'mmHg'
    assert low.system == 'http://unitsofmeasure.org'
    assert low.code == 'mm[Hg]'
    
    with pytest.raises(ValidationError):
        ReferenceRangeLow(value=2.1, unit='mmHg', system='http://unitsofmeasure.com', code='mm[Hg]')


@pytest.mark.anyio
async def test_reference_range_high() -> None:
    """
    # Checks pandantic model ReferenceRangeHigh.

    # :param value: ReferenceRangeHigh value.
    # :param unit: ReferenceRangeHigh unit.
    # :param system: ReferenceRangeHigh system.
    # :param code: ReferenceRangeHigh code.
    """
    high = ReferenceRangeHigh(value=4.2, unit='mmHg', system='http://unitsofmeasure.org', code='mm[Hg]')

    assert high.value == 4.2
    assert high.unit == 'mmHg'
    assert high.system == 'http://unitsofmeasure.org'
    assert high.code == 'mm[Hg]'
    
    with pytest.raises(ValidationError):
        ReferenceRangeHigh(value=4.2, unit='mmHg', system='http://unitsofmeasure.com', code='mm[Hg]')



# @pytest.mark.anyio
# async def test_reference_range_item() -> None:
#     """
#     # Checks pandantic model ReferenceRangeItem.
#     high: Optional[ReferenceRangeHigh] = None
#     low: Optional[ReferenceRangeLow] = None
#     normalValue: Optional[list[str]] = None
#     type: Optional[list[str]] = None
#     appliesTo: Optional[list[list[str]]] = None
#     age: Optional[list[int]] = None

#     # :param value: ReferenceRangeLow value.
#     # :param unit: ReferenceRangeLow unit.
#     # :param system: ReferenceRangeLow system.
#     # :param code: ReferenceRangeLow code.
#     """
#     low = ReferenceRangeItem(high=4.2, low=2.1, normalValue=2.0)

#     assert low.value == 2.1
#     assert low.unit == 'mmHg'
#     assert low.system == 'http://unitsofmeasure.org'
#     assert low.code == 'mm[Hg]'
    
    # with pytest.raises(ValidationError):
    #     ReferenceRangeLow(value=2.1, unit='mmHg', system='http://unitsofmeasure.com', code='mm[Hg]')