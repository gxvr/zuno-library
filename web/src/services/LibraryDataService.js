import http from "../http-common";

class LibraryDataService {
    getAll() {
        return http.get("/books");
    }

    get(bibnum, data) {
        return http.get(`/books/${bibnum}`, data);
    }
}

export default new LibraryDataService();