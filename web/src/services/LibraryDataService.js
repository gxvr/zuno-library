import http from "../http-common";

class LibraryDataService {
    getAll() {
        return http.get("/books");
    }

    get(bibnum) {
        return http.get(`/books/${bibnum}`);
    }
}

export default new LibraryDataService();