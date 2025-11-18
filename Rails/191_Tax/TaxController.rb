class TaxController < ApplicationController
  before_action :set_tax, only: [:show, :edit, :update, :destroy]

  # GET /tax
  def index
    @taxs = Tax.all
    render json: @taxs
  end

  # GET /tax/1
  def show
    render json: @tax
  end

  # POST /tax
  def create
    @tax = Tax.new(tax_params)

    if @tax.save
      render json: @tax, status: :created
    else
      render json: @tax.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /tax/1
  def update
    if @tax.update(tax_params)
      render json: @tax
    else
      render json: @tax.errors, status: :unprocessable_entity
    end
  end

  # DELETE /tax/1
  def destroy
    @tax.destroy
    head :no_content
  end

  private

  def set_tax
    @tax = Tax.find(params[:id])
  end

  def tax_params
    params.require(:tax).permit(:name)
  end
end
