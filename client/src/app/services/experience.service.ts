import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Experience } from '../models/experience.model';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ExperienceService {
  private readonly http = inject(HttpClient);
  private readonly apiUrl = `${environment.apiUrl}/experiences`;

  getAll(currentOnly: boolean = false): Observable<Experience[]> {
    return this.http.get<Experience[]>(`${this.apiUrl}?current_only=${currentOnly}`);
  }

  getById(id: string): Observable<Experience> {
    return this.http.get<Experience>(`${this.apiUrl}/${id}`);
  }
}
