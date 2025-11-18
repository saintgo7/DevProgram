class VendorController < ApplicationController
  before_action :set_vendor, only: [:show, :edit, :update, :destroy]

  # GET /vendor
  def index
    @vendors = Vendor.all
    render json: @vendors
  end

  # GET /vendor/1
  def show
    render json: @vendor
  end

  # POST /vendor
  def create
    @vendor = Vendor.new(vendor_params)

    if @vendor.save
      render json: @vendor, status: :created
    else
      render json: @vendor.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /vendor/1
  def update
    if @vendor.update(vendor_params)
      render json: @vendor
    else
      render json: @vendor.errors, status: :unprocessable_entity
    end
  end

  # DELETE /vendor/1
  def destroy
    @vendor.destroy
    head :no_content
  end

  private

  def set_vendor
    @vendor = Vendor.find(params[:id])
  end

  def vendor_params
    params.require(:vendor).permit(:name)
  end
end
