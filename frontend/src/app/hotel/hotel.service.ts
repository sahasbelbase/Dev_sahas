import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HotelService {

  baseUrl = 'http://localhost:5500/api/Hotel/';

  constructor(
    public http :HttpClient
  ) { }
  

GetHotelData(json: string): Observable<any> {
  const params = new HttpParams().set('json', '{}');
  return this.http.get(this.baseUrl + 'Hotel', { params});
}
HotelTsk(json:string): Observable<any>{
  return this.http.post(this.baseUrl + 'HotelTsk', { json: json});
}

}
