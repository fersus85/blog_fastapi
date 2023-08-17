from sqlalchemy.orm import Session
from src.schemas.blog import CreateBlog
from src.db.models.blog import Blog


def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    blog = Blog(**blog.dict(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog
