class AuditController < ApplicationController
  before_action :set_audit, only: [:show, :edit, :update, :destroy]

  # GET /audit
  def index
    @audits = Audit.all
    render json: @audits
  end

  # GET /audit/1
  def show
    render json: @audit
  end

  # POST /audit
  def create
    @audit = Audit.new(audit_params)

    if @audit.save
      render json: @audit, status: :created
    else
      render json: @audit.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /audit/1
  def update
    if @audit.update(audit_params)
      render json: @audit
    else
      render json: @audit.errors, status: :unprocessable_entity
    end
  end

  # DELETE /audit/1
  def destroy
    @audit.destroy
    head :no_content
  end

  private

  def set_audit
    @audit = Audit.find(params[:id])
  end

  def audit_params
    params.require(:audit).permit(:name)
  end
end
