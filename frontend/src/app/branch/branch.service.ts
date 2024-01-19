// src/app/branch/branch.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BranchService {
  private baseUrl = 'http://localhost:5500/api/branches';

  constructor(private http: HttpClient) {}

  // Define the method to fetch all branches
  getAllBranches(): Observable<any> {
    return this.http.get(this.baseUrl);
  }

  // Define the method for other branch-related tasks if needed
  branchTask(json: string): Observable<any> {
    return this.http.post(this.baseUrl, { json });
  }
}
