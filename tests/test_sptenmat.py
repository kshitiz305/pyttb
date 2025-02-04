# Copyright 2022 National Technology & Engineering Solutions of Sandia,
# LLC (NTESS). Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

import pytest

import pyttb as ttb


@pytest.mark.indevelopment
def test_sptenmat_initialization_empty():
    with pytest.raises(AssertionError) as excinfo:
        ttb.sptenmat()
    assert "SPTENMAT class not yet implemented" in str(excinfo)
