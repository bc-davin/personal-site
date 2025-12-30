import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Blog } from '../models/blog.model';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class BlogService {
  private readonly http = inject(HttpClient);
  private readonly apiUrl = `${environment.apiUrl}/blogs`;

  getAll(publishedOnly: boolean = false): Observable<Blog[]> {
    return this.http.get<Blog[]>(`${this.apiUrl}?published_only=${publishedOnly}`);
  }

  getById(id: string): Observable<Blog> {
    return this.http.get<Blog>(`${this.apiUrl}/${id}`);
  }
}
