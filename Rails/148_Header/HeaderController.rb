class HeaderController < ApplicationController
  before_action :set_header, only: [:show, :edit, :update, :destroy]

  # GET /header
  def index
    @headers = Header.all
    render json: @headers
  end

  # GET /header/1
  def show
    render json: @header
  end

  # POST /header
  def create
    @header = Header.new(header_params)

    if @header.save
      render json: @header, status: :created
    else
      render json: @header.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /header/1
  def update
    if @header.update(header_params)
      render json: @header
    else
      render json: @header.errors, status: :unprocessable_entity
    end
  end

  # DELETE /header/1
  def destroy
    @header.destroy
    head :no_content
  end

  private

  def set_header
    @header = Header.find(params[:id])
  end

  def header_params
    params.require(:header).permit(:name)
  end
end
