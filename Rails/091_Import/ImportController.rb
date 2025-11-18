class ImportController < ApplicationController
  before_action :set_import, only: [:show, :edit, :update, :destroy]

  # GET /import
  def index
    @imports = Import.all
    render json: @imports
  end

  # GET /import/1
  def show
    render json: @import
  end

  # POST /import
  def create
    @import = Import.new(import_params)

    if @import.save
      render json: @import, status: :created
    else
      render json: @import.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /import/1
  def update
    if @import.update(import_params)
      render json: @import
    else
      render json: @import.errors, status: :unprocessable_entity
    end
  end

  # DELETE /import/1
  def destroy
    @import.destroy
    head :no_content
  end

  private

  def set_import
    @import = Import.find(params[:id])
  end

  def import_params
    params.require(:import).permit(:name)
  end
end
