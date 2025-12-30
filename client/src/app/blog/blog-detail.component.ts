import { Component, OnInit, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { BlogService } from '../services/blog.service';
import { Blog } from '../models/blog.model';

@Component({
  selector: 'app-blog-detail',
  imports: [CommonModule],
  templateUrl: './blog-detail.component.html',
  styleUrl: './blog-detail.component.scss'
})
export class BlogDetailComponent implements OnInit {
  private readonly blogService = inject(BlogService);
  private readonly route = inject(ActivatedRoute);
  private readonly router = inject(Router);

  protected readonly blog = signal<Blog | null>(null);
  protected readonly loading = signal(true);
  protected readonly error = signal<string | null>(null);

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.loadBlog(id);
    } else {
      this.router.navigate(['/blog']);
    }
  }

  private loadBlog(id: string): void {
    this.loading.set(true);
    this.error.set(null);

    this.blogService.getById(id).subscribe({
      next: (blog) => {
        this.blog.set(blog);
        this.loading.set(false);
      },
      error: (err) => {
        console.error('Error loading blog:', err);
        this.error.set('Blog post not found.');
        this.loading.set(false);
      }
    });
  }

  protected goBack(): void {
    this.router.navigate(['/blog']);
  }
}
