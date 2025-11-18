class GSTController < ApplicationController
  before_action :set_gst, only: [:show, :edit, :update, :destroy]

  # GET /gst
  def index
    @gsts = GST.all
    render json: @gsts
  end

  # GET /gst/1
  def show
    render json: @gst
  end

  # POST /gst
  def create
    @gst = GST.new(gst_params)

    if @gst.save
      render json: @gst, status: :created
    else
      render json: @gst.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /gst/1
  def update
    if @gst.update(gst_params)
      render json: @gst
    else
      render json: @gst.errors, status: :unprocessable_entity
    end
  end

  # DELETE /gst/1
  def destroy
    @gst.destroy
    head :no_content
  end

  private

  def set_gst
    @gst = GST.find(params[:id])
  end

  def gst_params
    params.require(:gst).permit(:name)
  end
end
