export interface Project {
  _id: string;
  title: string;
  description: string;
  technologies: string[];
  github_url?: string;
  live_url?: string;
  image_url?: string;
  featured: boolean;
  start_date?: string;
  end_date?: string;
  created_at: string;
  updated_at: string;
}

export interface ProjectCreate {
  title: string;
  description: string;
  technologies?: string[];
  github_url?: string;
  live_url?: string;
  image_url?: string;
  featured?: boolean;
  start_date?: string;
  end_date?: string;
}
