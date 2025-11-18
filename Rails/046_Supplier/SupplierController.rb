class SupplierController < ApplicationController
  before_action :set_supplier, only: [:show, :edit, :update, :destroy]

  # GET /supplier
  def index
    @suppliers = Supplier.all
    render json: @suppliers
  end

  # GET /supplier/1
  def show
    render json: @supplier
  end

  # POST /supplier
  def create
    @supplier = Supplier.new(supplier_params)

    if @supplier.save
      render json: @supplier, status: :created
    else
      render json: @supplier.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /supplier/1
  def update
    if @supplier.update(supplier_params)
      render json: @supplier
    else
      render json: @supplier.errors, status: :unprocessable_entity
    end
  end

  # DELETE /supplier/1
  def destroy
    @supplier.destroy
    head :no_content
  end

  private

  def set_supplier
    @supplier = Supplier.find(params[:id])
  end

  def supplier_params
    params.require(:supplier).permit(:name)
  end
end
