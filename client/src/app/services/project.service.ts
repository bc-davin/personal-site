import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Project } from '../models/project.model';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProjectService {
  private readonly http = inject(HttpClient);
  private readonly apiUrl = `${environment.apiUrl}/projects`;

  getAll(featuredOnly: boolean = false): Observable<Project[]> {
    return this.http.get<Project[]>(`${this.apiUrl}?featured_only=${featuredOnly}`);
  }

  getById(id: string): Observable<Project> {
    return this.http.get<Project>(`${this.apiUrl}/${id}`);
  }
}
