import { Component, OnInit, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ExperienceService } from '../services/experience.service';
import { Experience } from '../models/experience.model';

@Component({
  selector: 'app-experience',
  imports: [CommonModule],
  templateUrl: './experience.component.html',
  styleUrl: './experience.component.scss'
})
export class ExperienceComponent implements OnInit {
  private readonly experienceService = inject(ExperienceService);

  protected readonly experiences = signal<Experience[]>([]);
  protected readonly loading = signal(true);
  protected readonly error = signal<string | null>(null);

  ngOnInit(): void {
    this.loadExperiences();
  }

  private loadExperiences(): void {
    this.loading.set(true);
    this.error.set(null);

    this.experienceService.getAll().subscribe({
      next: (experiences) => {
        console.log('Experience data from backend:', JSON.stringify(experiences, null, 2));
        this.experiences.set(experiences);
        this.loading.set(false);
      },
      error: (err) => {
        console.error('Error loading experiences:', err);
        this.error.set('Failed to load experience data. Please try again later.');
        this.loading.set(false);
      }
    });
  }

  protected formatDate(date: string): string {
    return new Date(date).toLocaleDateString('en-US', { month: 'short', year: 'numeric' });
  }

  protected getDuration(start: string, end: string | undefined): string {
    const startDate = new Date(start);
    const endDate = end ? new Date(end) : new Date();
    
    const months = (endDate.getFullYear() - startDate.getFullYear()) * 12 + 
                   (endDate.getMonth() - startDate.getMonth());
    
    const years = Math.floor(months / 12);
    const remainingMonths = months % 12;
    
    if (years === 0) {
      return `${remainingMonths} ${remainingMonths === 1 ? 'month' : 'months'}`;
    } else if (remainingMonths === 0) {
      return `${years} ${years === 1 ? 'year' : 'years'}`;
    } else {
      return `${years} ${years === 1 ? 'year' : 'years'} ${remainingMonths} ${remainingMonths === 1 ? 'month' : 'months'}`;
    }
  }
}
