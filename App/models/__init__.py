from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .employer import Employer
from .staff import Staff
from .student import Student
from .internship_position import InternshipPosition
from .shortlist import Shortlist

__all__ = ['db','User', 'Employer', 'Staff', 'Student', 'InternshipPosition', 'Shortlist']