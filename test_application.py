import sys

import pygame
from pygame.sprite import Group
from pygame.time import Clock

# app core modules
from modules.app.settings import Settings
from modules.app.renderer import Renderer

# app specific modules
from modules.gui.gui import Gui
from modules.calculator import Calculator
from modules.notes import Notes
from modules.koppelcode import KoppelCode

# testing
import pytest
from main import Application

@pytest.fixture
def app_instance():
    app = Application()

    #app.m_gui.openTab( app.m_gui.TAB_CALCULATOR )
    #app.run()

    return app

def test_module_instances( app_instance ):
    """Test if modules are set and match the correct class data type"""
    assert isinstance( app_instance.m_settings,     Settings )
    assert isinstance( app_instance.m_clock,        Clock )
    assert isinstance( app_instance.m_renderer,     Renderer )

    # app specific modules
    assert isinstance( app_instance.m_gui,          Gui )
    assert isinstance( app_instance.m_notes,        Notes )
    assert isinstance( app_instance.m_koppelcode,   KoppelCode )
    assert isinstance( app_instance.m_calculator,   Calculator )

def test_koppelcode( app_instance ):
    """Test if koppelcode returns string and correct amount of letters"""
    num_letters = 6

    # generate koppelcode
    code = app_instance.m_koppelcode.get_random_code( num_letters )
    print( f"code generated: {code}" )

    # check if generator code is a string
    assert isinstance( code, str )

    # check if number of letter matches the requested amount of letters
    assert( len(code) == num_letters )

def test_calculator( app_instance ):
    """Test calculator methods"""
    assert( app_instance.m_calculator.parse_equation_string( "1+1" ) == 2 )
    assert( app_instance.m_calculator.parse_equation_string( "2*2" ) == 4 )
    assert( app_instance.m_calculator.parse_equation_string( "4/2" ) == 2 )
    assert( app_instance.m_calculator.parse_equation_string( "2-1" ) == 1 )
    assert( app_instance.m_calculator.parse_equation_string( "0.1+0.1" ) == 0.2 )
    assert( app_instance.m_calculator.parse_equation_string( "100-0.05" ) == 99.95 )