export interface Blog {
  _id: string;
  title: string;
  content: string;
  excerpt?: string;
  tags: string[];
  published: boolean;
  featured_image?: string;
  author: string;
  created_at: string;
  updated_at: string;
}

export interface BlogCreate {
  title: string;
  content: string;
  excerpt?: string;
  tags?: string[];
  published?: boolean;
  featured_image?: string;
  author?: string;
}
