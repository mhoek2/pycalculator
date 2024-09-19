from ast import Tuple
import sys
import pygame

class Settings:
    """Application settings containing eg. target_fps, resolution"""
    m_window_title              : str
    m_target_fps                : int
    m_icon                      : pygame.Surface
    m_resolution                : Tuple
    m_window_flags              : int
    m_clear_color               : pygame.Color
    m_background_image_path     : str

    def __init__( self ) -> None:
        self.m_window_title             = "Calculator"
        self.m_target_fps               = 60
        self.m_icon                     = False
        self.m_resolution               = ( 400, 600 )
        self.m_window_flags             = 0
        self.m_clear_color              = ( 0, 0, 0 )
        self.m_background_image_path    = "assets/app/background.png"

    def setBackgroundIcon( self, path ) -> None:
        """Icon for the appplication"""
        self.m_icon = pygame.image.load( path )  
        pygame.display.set_icon( self.m_icon )

    def setClearColor( self, color ) -> None:
        """Color each frame clears to at the beginning of a new frame"""
        self.m_clear_color = color

