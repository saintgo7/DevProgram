class ConverterController < ApplicationController
  before_action :set_converter, only: [:show, :edit, :update, :destroy]

  # GET /converter
  def index
    @converters = Converter.all
    render json: @converters
  end

  # GET /converter/1
  def show
    render json: @converter
  end

  # POST /converter
  def create
    @converter = Converter.new(converter_params)

    if @converter.save
      render json: @converter, status: :created
    else
      render json: @converter.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /converter/1
  def update
    if @converter.update(converter_params)
      render json: @converter
    else
      render json: @converter.errors, status: :unprocessable_entity
    end
  end

  # DELETE /converter/1
  def destroy
    @converter.destroy
    head :no_content
  end

  private

  def set_converter
    @converter = Converter.find(params[:id])
  end

  def converter_params
    params.require(:converter).permit(:name)
  end
end
