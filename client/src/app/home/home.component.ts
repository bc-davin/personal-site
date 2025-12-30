import { Component, OnInit, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { ProjectService } from '../services/project.service';
import { BlogService } from '../services/blog.service';
import { Project } from '../models/project.model';
import { Blog } from '../models/blog.model';

@Component({
  selector: 'app-home',
  imports: [CommonModule, RouterLink],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {
  private readonly projectService = inject(ProjectService);
  private readonly blogService = inject(BlogService);

  protected readonly featuredProjects = signal<Project[]>([]);
  protected readonly recentBlogs = signal<Blog[]>([]);
  protected readonly loading = signal(true);
  protected readonly error = signal<string | null>(null);

  ngOnInit(): void {
    this.loadFeaturedContent();
  }

  private loadFeaturedContent(): void {
    this.loading.set(true);
    this.error.set(null);

    Promise.all([
      this.projectService.getAll(true).toPromise(),
      this.blogService.getAll(true).toPromise()
    ])
      .then(([projects, blogs]) => {
        this.featuredProjects.set(projects?.slice(0, 3) || []);
        this.recentBlogs.set(blogs?.slice(0, 3) || []);
      })
      .catch(err => {
        console.error('Error loading featured content:', err);
        this.error.set('Failed to load content. Please try again later.');
      })
      .finally(() => {
        this.loading.set(false);
      });
  }
}
