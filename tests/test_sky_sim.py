from mymodule.sky_sim import get_radec, make_stars#, sexadecimal_to_float, float_to_sexadecimal
import pytest

def test_module_import():
    try:
        import mymodule.sky_sim
    except Exception as e:
        raise AssertionError("Failed to import mymodule")
    return

def test_get_radec_values():
    """
    This checks that get_radec gives back the correct coordinates of Andromeda in decimal degrees.
    """
    ra, dec = get_radec()

    assert ra == pytest.approx(14.215420962967535) #, rel=1e-20 --> tolerance during this approximation
    assert dec == pytest.approx(41.26916666666667)

#@pytest.mark.parametrize("ra, dec", 
#                         [(14.215420962967535, 41.26916666666667),
#                         ])

#def test_sexadecimal_to_float(ra, dec):
#    new_ra, new_dec = sexadecimal_to_float(*float_to_sexadecimal(ra,dec))

#    assert new_ra == pytest.approx(ra)
#    assert new_dec == pytest.approx(dec)

def test_make_star_values():
    """
    This generates 1000 random spatial points around the given coordinates. 
    """
    NSRC =  1000

    ra, dec = get_radec()
    ras, decs = make_stars(ra, dec)

    assert NSRC == len(ras)
    assert NSRC == len(decs)

    
