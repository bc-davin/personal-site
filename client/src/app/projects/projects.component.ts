import { Component, OnInit, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { ProjectService } from '../services/project.service';
import { Project } from '../models/project.model';

@Component({
  selector: 'app-projects',
  imports: [CommonModule, RouterLink],
  templateUrl: './projects.component.html',
  styleUrl: './projects.component.scss'
})
export class ProjectsComponent implements OnInit {
  private readonly projectService = inject(ProjectService);

  protected readonly projects = signal<Project[]>([]);
  protected readonly loading = signal(true);
  protected readonly error = signal<string | null>(null);

  ngOnInit(): void {
    this.loadProjects();
  }

  private loadProjects(): void {
    this.loading.set(true);
    this.error.set(null);

    this.projectService.getAll().subscribe({
      next: (projects) => {
        this.projects.set(projects);
        this.loading.set(false);
      },
      error: (err) => {
        console.error('Error loading projects:', err);
        this.error.set('Failed to load projects. Please try again later.');
        this.loading.set(false);
      }
    });
  }
}
