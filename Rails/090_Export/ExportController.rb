class ExportController < ApplicationController
  before_action :set_export, only: [:show, :edit, :update, :destroy]

  # GET /export
  def index
    @exports = Export.all
    render json: @exports
  end

  # GET /export/1
  def show
    render json: @export
  end

  # POST /export
  def create
    @export = Export.new(export_params)

    if @export.save
      render json: @export, status: :created
    else
      render json: @export.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /export/1
  def update
    if @export.update(export_params)
      render json: @export
    else
      render json: @export.errors, status: :unprocessable_entity
    end
  end

  # DELETE /export/1
  def destroy
    @export.destroy
    head :no_content
  end

  private

  def set_export
    @export = Export.find(params[:id])
  end

  def export_params
    params.require(:export).permit(:name)
  end
end
