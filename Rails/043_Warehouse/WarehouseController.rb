class WarehouseController < ApplicationController
  before_action :set_warehouse, only: [:show, :edit, :update, :destroy]

  # GET /warehouse
  def index
    @warehouses = Warehouse.all
    render json: @warehouses
  end

  # GET /warehouse/1
  def show
    render json: @warehouse
  end

  # POST /warehouse
  def create
    @warehouse = Warehouse.new(warehouse_params)

    if @warehouse.save
      render json: @warehouse, status: :created
    else
      render json: @warehouse.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /warehouse/1
  def update
    if @warehouse.update(warehouse_params)
      render json: @warehouse
    else
      render json: @warehouse.errors, status: :unprocessable_entity
    end
  end

  # DELETE /warehouse/1
  def destroy
    @warehouse.destroy
    head :no_content
  end

  private

  def set_warehouse
    @warehouse = Warehouse.find(params[:id])
  end

  def warehouse_params
    params.require(:warehouse).permit(:name)
  end
end
