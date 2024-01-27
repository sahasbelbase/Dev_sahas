import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Branch } from './branch.model';

@Injectable({
  providedIn: 'root',
})
export class BranchService {
  private baseUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) {}

  getHotels(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/hotels`);
  }

  getAddressTypes(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/addressTypes`);
  }

  addBranch(formData: any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/addBranch`, formData);
  }

 
  getBranchesWithAddress(): Observable<Branch[]> {
    return this.http.get<Branch[]>(`${this.baseUrl}/branches`);
  }
}
