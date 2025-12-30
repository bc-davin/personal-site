import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProjectsComponent } from './projects/projects.component';
import { BlogComponent } from './blog/blog.component';
import { BlogDetailComponent } from './blog/blog-detail.component';
import { ExperienceComponent } from './experience/experience.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'projects', component: ProjectsComponent },
  { path: 'blog', component: BlogComponent },
  { path: 'blog/:id', component: BlogDetailComponent },
  { path: 'experience', component: ExperienceComponent },
  { path: '**', redirectTo: '' }
];
