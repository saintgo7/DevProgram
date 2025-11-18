class FormController < ApplicationController
  before_action :set_form, only: [:show, :edit, :update, :destroy]

  # GET /form
  def index
    @forms = Form.all
    render json: @forms
  end

  # GET /form/1
  def show
    render json: @form
  end

  # POST /form
  def create
    @form = Form.new(form_params)

    if @form.save
      render json: @form, status: :created
    else
      render json: @form.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /form/1
  def update
    if @form.update(form_params)
      render json: @form
    else
      render json: @form.errors, status: :unprocessable_entity
    end
  end

  # DELETE /form/1
  def destroy
    @form.destroy
    head :no_content
  end

  private

  def set_form
    @form = Form.find(params[:id])
  end

  def form_params
    params.require(:form).permit(:name)
  end
end
