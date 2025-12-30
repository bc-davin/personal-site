import { Component, OnInit, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { BlogService } from '../services/blog.service';
import { Blog } from '../models/blog.model';

@Component({
  selector: 'app-blog',
  imports: [CommonModule, RouterLink],
  templateUrl: './blog.component.html',
  styleUrl: './blog.component.scss'
})
export class BlogComponent implements OnInit {
  private readonly blogService = inject(BlogService);

  protected readonly blogs = signal<Blog[]>([]);
  protected readonly loading = signal(true);
  protected readonly error = signal<string | null>(null);

  ngOnInit(): void {
    this.loadBlogs();
  }

  private loadBlogs(): void {
    this.loading.set(true);
    this.error.set(null);

    this.blogService.getAll(true).subscribe({
      next: (blogs) => {
        this.blogs.set(blogs);
        this.loading.set(false);
      },
      error: (err) => {
        console.error('Error loading blogs:', err);
        this.error.set('Failed to load blog posts. Please try again later.');
        this.loading.set(false);
      }
    });
  }

  protected getExcerpt(blog: Blog): string {
    return blog.excerpt || blog.content.substring(0, 200) + '...';
  }
}
