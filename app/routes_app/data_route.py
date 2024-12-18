from flask import Blueprint, json, jsonify, redirect, render_template, request, url_for
from flask_login import login_required
from ..services import data_svc 

data_route = Blueprint('data_route', __name__)
rows_per_page = 10

@data_route.route('/data_mahasiswa', methods=['GET'])
@login_required
def data_mahasiswa():
    page = request.args.get('page', 1, type=int)
    mahasiswa_all = data_svc.getMahasiswadanProdiwithParam()
    
    total_rows = len(mahasiswa_all)
    start_index = (page - 1) * rows_per_page
    end_index = start_index + rows_per_page
    paginated_data = mahasiswa_all[start_index:end_index]
    pagination = {
        'has_prev': page > 1,
        'has_next': end_index < total_rows,
        'prev_num': page - 1,
        'next_num': page + 1,
        'page': page,
        'total': total_rows,
        'iter_pages': lambda: range(1, (total_rows // rows_per_page) + 2)  # Menghasilkan nomor halaman
    }

    # return render_template('data.html', mahasiswa_all=mahasiswa_all)
    return render_template('data.html', mahasiswa_all=paginated_data, pagination=pagination)

@data_route.route('/data_mahasiswa', methods=['GET', 'POST'])
@login_required
def data_mahasiswa_get():
    nim = request.form.get('nim') 
    nama = request.form.get('nama') 
    fakultas = request.form.get('fakultas') 
    prodi = request.form.get('prodi') 
    page = request.args.get('page', 1, type=int)
    mahasiswa_all = data_svc.getMahasiswadanProdiwithParam(nim, nama, fakultas, prodi)
    
    total_rows = len(mahasiswa_all)
    start_index = (page - 1) * rows_per_page
    end_index = start_index + rows_per_page
    paginated_data = mahasiswa_all[start_index:end_index]
    pagination = {
        'has_prev': page > 1,
        'has_next': end_index < total_rows,
        'prev_num': page - 1,
        'next_num': page + 1,
        'page': page,
        'total': total_rows,
        'iter_pages': lambda: range(1, (total_rows // rows_per_page) + 2)  # Menghasilkan nomor halaman
    }
    
    # return render_template('data.html', mahasiswa_all=mahasiswa_all, nama=nama, nim=nim, fakultas=fakultas, prodi=prodi)
    return render_template('data.html', nama=nama, nim=nim, fakultas=fakultas, prodi=prodi,
                           mahasiswa_all=paginated_data, pagination=pagination)

@data_route.route('/delete_mahasiswa', methods=['POST'])
def delete_mahasiswa():
    nim = request.form.get('nim')
    result = data_svc.deleteDataKuesionerMahasiswa(nim)
    if (result == 'Berhasil') :
        return jsonify({"success": True}), 200
    else :
        return jsonify({"success": False}), 404
    # return redirect(url_for('data_route.data_mahasiswa'))