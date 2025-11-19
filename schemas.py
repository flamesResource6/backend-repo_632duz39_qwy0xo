"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List

# Example schemas (kept for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: Optional[str] = Field(None, description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Digital Giants specific schemas

class Author(BaseModel):
    """Authors of books"""
    name: str = Field(..., description="Author name")
    bio: Optional[str] = Field(None, description="Short biography")
    website: Optional[HttpUrl] = Field(None, description="Personal website")
    avatar_url: Optional[HttpUrl] = Field(None, description="Avatar or portrait image")

class Book(BaseModel):
    """Published books"""
    title: str = Field(..., description="Book title")
    subtitle: Optional[str] = Field(None, description="Subtitle")
    description: Optional[str] = Field(None, description="Short description")
    author: str = Field(..., description="Primary author name")
    genres: List[str] = Field(default_factory=list, description="List of genres/tags")
    cover_url: Optional[HttpUrl] = Field(None, description="Cover image URL")
    pages: Optional[int] = Field(None, ge=1, description="Number of pages")
    price: Optional[float] = Field(None, ge=0, description="Price in USD")
    isbn: Optional[str] = Field(None, description="ISBN number")
    featured: bool = Field(False, description="Whether the book is featured")

class Submission(BaseModel):
    """Incoming publishing submissions"""
    author_name: str = Field(..., description="Your full name")
    email: EmailStr = Field(..., description="Contact email")
    book_title: str = Field(..., description="Working title of the book")
    synopsis: str = Field(..., min_length=50, description="Brief synopsis of the manuscript")
    genre: Optional[str] = Field(None, description="Primary genre")
    word_count: Optional[int] = Field(None, ge=1000, description="Estimated word count")
    manuscript_url: Optional[HttpUrl] = Field(None, description="Link to sample chapters or manuscript")

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
