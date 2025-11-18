class VATController < ApplicationController
  before_action :set_vat, only: [:show, :edit, :update, :destroy]

  # GET /vat
  def index
    @vats = VAT.all
    render json: @vats
  end

  # GET /vat/1
  def show
    render json: @vat
  end

  # POST /vat
  def create
    @vat = VAT.new(vat_params)

    if @vat.save
      render json: @vat, status: :created
    else
      render json: @vat.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /vat/1
  def update
    if @vat.update(vat_params)
      render json: @vat
    else
      render json: @vat.errors, status: :unprocessable_entity
    end
  end

  # DELETE /vat/1
  def destroy
    @vat.destroy
    head :no_content
  end

  private

  def set_vat
    @vat = VAT.find(params[:id])
  end

  def vat_params
    params.require(:vat).permit(:name)
  end
end
