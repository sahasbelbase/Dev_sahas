import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BranchService {

  baseUrl = 'http://localhost:5500/api/Branch/';
  constructor(
    public http :HttpClient
  ) { }
  

GetBranchData(branchData: string): Observable<any> {
  const params = new HttpParams().set('json', '{}');
  return this.http.get(this.baseUrl + 'Branch', { params});
}
BranchTsk(json:string): Observable<any>{
  return this.http.post(this.baseUrl + 'BranchTsk', { json: json});
}

}